from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    """
    Represents an open position.
    """

    symbol: str = ""
    exchange: str = ""
    currency: str = ""

    quantity: float = 0.0
    average_cost: float = 0.0

    market_price: float = 0.0
    market_value: float = 0.0

    unrealized_pnl: float = 0.0
    realized_pnl: float = 0.0