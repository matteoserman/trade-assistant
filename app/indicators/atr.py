import pandas as pd


class ATR:
    """
    Average True Range indicator.
    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
        period: int = 14,
    ) -> pd.DataFrame:

        result = df.copy()

        high_low = result["High"] - result["Low"]

        high_close = (
            result["High"] - result["Close"].shift()
        ).abs()

        low_close = (
            result["Low"] - result["Close"].shift()
        ).abs()

        tr = pd.concat(
            [
                high_low,
                high_close,
                low_close,
            ],
            axis=1,
        ).max(axis=1)

        result[f"ATR_{period}"] = (
            tr.rolling(period).mean()
        )

        return result