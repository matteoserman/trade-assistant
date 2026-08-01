import threading

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

        self.wrapper.account_summary_event.clear()

        self.client.reqAccountSummary(
            1,
            "All",
            "NetLiquidation,BuyingPower,TotalCashValue",
        )

        received = self.wrapper.account_summary_event.wait(timeout=5)

        self.client.cancelAccountSummary(1)

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