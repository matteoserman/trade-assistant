import threading

from ibapi.contract import Contract
from app.services.broker.ibapi.contracts import ContractFactory

from app.services.broker.interface import BrokerInterface
from app.services.broker.ibapi.client import IBApiClient
from app.services.broker.ibapi.wrapper import IBApiWrapper
from app.utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)


class IBApiBroker(BrokerInterface):
    """
    Facade over the Interactive Brokers API.
    """

    def __init__(self):
        self.wrapper = IBApiWrapper()
        self.client = IBApiClient(self.wrapper)

        self._thread = None
        self._request_id = 1

    def _next_request_id(self) -> int:
        request_id = self._request_id
        self._request_id += 1
        return request_id

    def connect(self) -> bool:

        logger.info("Connecting to Interactive Brokers...")

        self.client.connect(
            settings.ib_host,
            settings.ib_port,
            settings.ib_client_id,
        )

        self._thread = threading.Thread(
            target=self.client.run,
            daemon=True,
        )

        self._thread.start()

        connected = self.wrapper.connected_event.wait(timeout=5)

        if connected:
            logger.info("Connected successfully.")
        else:
            logger.error("Connection timed out.")

        return connected

    def disconnect(self) -> None:

        if self.client.isConnected():
            self.client.disconnect()
            logger.info("Disconnected.")

    def is_connected(self) -> bool:

        return self.client.isConnected()

    def get_account_summary(self):

        logger.info("Requesting account summary...")

        request_id = self._next_request_id()

        self.wrapper.account_summary_event.clear()

        self.client.reqAccountSummary(
            request_id,
            "All",
            "NetLiquidation,BuyingPower,TotalCashValue",
        )

        received = self.wrapper.account_summary_event.wait(timeout=5)

        self.client.cancelAccountSummary(request_id)

        if not received:
            logger.error("Timed out waiting for account summary.")
            return None

        logger.info("Account summary retrieved successfully.")

        return self.wrapper.account

    def get_positions(self):

        logger.info("Requesting positions...")

        self.wrapper.positions.clear()
        self.wrapper.positions_event.clear()

        self.client.reqPositions()

        received = self.wrapper.positions_event.wait(timeout=5)

        self.client.cancelPositions()

        if not received:
            logger.error("Timed out waiting for positions.")
            return []

        logger.info(
            "Retrieved %s position(s).",
            len(self.wrapper.positions),
        )

        return self.wrapper.positions

    def get_historical_data(
        self,
        symbol: str,
        duration: str,
        bar_size: str,
    ):

        logger.info("Requesting historical data for %s...", symbol)

        request_id = self._next_request_id()

        self.wrapper.historical_data.clear()
        self.wrapper.historical_data_event.clear()

        contract = ContractFactory.stock(symbol)

        self.client.reqHistoricalData(
            request_id,
            contract,
            "",
            duration,
            bar_size,
            "TRADES",
            1,
            1,
            False,
            [],
        )

        received = self.wrapper.historical_data_event.wait(timeout=15)

        if not received:
            logger.error("Timed out waiting for historical data.")
            return []

        logger.info(
            "Retrieved %s bars.",
            len(self.wrapper.historical_data),
        )

        return self.wrapper.historical_data