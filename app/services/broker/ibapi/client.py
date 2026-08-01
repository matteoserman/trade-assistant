from ibapi.client import EClient

from app.services.broker.ibapi.wrapper import IBApiWrapper


class IBApiClient(EClient):
    """
    Sends requests to Interactive Brokers.

    This class is responsible only for communicating with the IB API.
    """

    def __init__(self, wrapper: IBApiWrapper):
        super().__init__(wrapper)