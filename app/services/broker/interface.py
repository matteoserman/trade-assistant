from abc import ABC, abstractmethod
from typing import Any

from app.domain.bar import Bar


class BrokerInterface(ABC):
    """
    Abstract interface that all broker implementations must follow.
    """

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def get_account_summary(self) -> Any:
        pass

    @abstractmethod
    def get_positions(self) -> Any:
        pass

    @abstractmethod
    def get_historical_data(
        self,
        symbol: str,
        duration: str,
        bar_size: str,
    ) -> list[Bar]:
        """
        Returns historical OHLCV bars.
        """
        pass