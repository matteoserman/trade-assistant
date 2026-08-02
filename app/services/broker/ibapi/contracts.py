from ibapi.contract import Contract


class ContractFactory:
    """
    Factory for creating Interactive Brokers contracts.
    """

    @staticmethod
    def stock(symbol: str) -> Contract:
        contract = Contract()

        contract.symbol = symbol.upper()
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        return contract