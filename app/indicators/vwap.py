import pandas as pd


class VWAP:
    """
    Volume Weighted Average Price (VWAP).

    Assumes the DataFrame contains:
        High
        Low
        Close
        Volume
    """

    @staticmethod
    def calculate(df: pd.DataFrame) -> pd.DataFrame:

        result = df.copy()

        typical_price = (
            result["High"] +
            result["Low"] +
            result["Close"]
        ) / 3

        cumulative_tp_volume = (
            typical_price * result["Volume"]
        ).cumsum()

        cumulative_volume = (
            result["Volume"]
        ).cumsum()

        result["VWAP"] = (
            cumulative_tp_volume /
            cumulative_volume
        )

        return result