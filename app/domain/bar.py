from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Bar:
    """
    Represents a single OHLCV market bar.
    """

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float