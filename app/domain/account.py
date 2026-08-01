from dataclasses import dataclass


@dataclass(slots=True)
class AccountSummary:
    """
    Represents the trading account summary used throughout the application.
    """

    account_id: str = ""
    net_liquidation: float = 0.0
    buying_power: float = 0.0
    cash_balance: float = 0.0
    currency: str = "USD"