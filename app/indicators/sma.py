import pandas as pd


class SMA:
    """
    Simple Moving Average indicator.
    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
        period: int,
        column: str = "Close",
    ) -> pd.DataFrame:

        result = df.copy()

        result[f"SMA_{period}"] = (
            result[column]
            .rolling(window=period)
            .mean()
        )

        return result