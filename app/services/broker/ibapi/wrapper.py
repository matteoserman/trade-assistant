from threading import Event

from ibapi.wrapper import EWrapper

from app.domain.account import AccountSummary
from app.domain.position import Position
from app.utils.logger import get_logger

logger = get_logger(__name__)


class IBApiWrapper(EWrapper):
    """
    Receives callbacks from Interactive Brokers.

    This class never contains business logic.
    It only stores translated domain objects.
    """

    def __init__(self):
        super().__init__()

        #
        # Connection
        #
        self.connected_event = Event()
        self.next_order_id = None

        #
        # Account
        #
        self.account_summary_event = Event()
        self.account = AccountSummary()

        #
        # Positions
        #
        self.positions_event = Event()
        self.positions = []

    def nextValidId(self, orderId: int):

        self.next_order_id = orderId

        logger.info(
            "Connected to Interactive Brokers. Next Order ID: %s",
            orderId,
        )

        self.connected_event.set()

    #
    # ----------------------------
    # Account Summary
    # ----------------------------
    #

    def accountSummary(
        self,
        reqId,
        account,
        tag,
        value,
        currency,
    ):

        self.account.account_id = account
        self.account.currency = currency

        try:

            if tag == "NetLiquidation":
                self.account.net_liquidation = float(value)

            elif tag == "BuyingPower":
                self.account.buying_power = float(value)

            elif tag == "TotalCashValue":
                self.account.cash_balance = float(value)

        except ValueError:

            logger.warning(
                "Could not convert value '%s' for tag '%s'",
                value,
                tag,
            )

    def accountSummaryEnd(self, reqId):

        logger.info("Account summary received.")

        self.account_summary_event.set()

    #
    # ----------------------------
    # Positions
    # ----------------------------
    #

    def position(
        self,
        account,
        contract,
        position,
        avgCost,
    ):

        self.positions.append(
            Position(
                symbol=contract.symbol,
                exchange=contract.exchange,
                currency=contract.currency,
                quantity=position,
                average_cost=avgCost,
            )
        )

    def positionEnd(self):

        logger.info(
            "Received %s position(s).",
            len(self.positions),
        )

        self.positions_event.set()

    #
    # ----------------------------
    # Errors
    # ----------------------------
    #

    def error(
        self,
        reqId,
        errorCode,
        errorString,
        advancedOrderRejectJson="",
    ):

        message = (
            f"ReqId={reqId} "
            f"Code={errorCode} "
            f"Message={errorString}"
        )

        if errorCode in (2104, 2106, 2107, 2108, 2158):
            logger.info(message)
        else:
            logger.error(message)