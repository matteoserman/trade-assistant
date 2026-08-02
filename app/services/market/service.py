import pandas as pd

from app.services.broker.interface import BrokerInterface


class MarketService:
    """
    Broker-independent market data service.
    """

    def __init__(self, broker: BrokerInterface):
        self._broker = broker

    def get_history(
        self,
        symbol: str,
        timeframe: str = "1 day",
        lookback: str = "1 Y",
    ) -> pd.DataFrame:
        """
        Returns historical OHLCV data as a Pandas DataFrame.
        """

        bars = self._broker.get_historical_data(
            symbol=symbol,
            duration=lookback,
            bar_size=timeframe,
        )

        if not bars:
            return pd.DataFrame()

        df = pd.DataFrame(
            {
                "Date": [b.timestamp for b in bars],
                "Open": [b.open for b in bars],
                "High": [b.high for b in bars],
                "Low": [b.low for b in bars],
                "Close": [b.close for b in bars],
                "Volume": [b.volume for b in bars],
            }
        )

        df.set_index("Date", inplace=True)
        df.sort_index(inplace=True)

        return df