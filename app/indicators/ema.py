import pandas as pd


class EMA:
    """
    Exponential Moving Average indicator.
    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
        period: int,
        column: str = "Close",
    ) -> pd.DataFrame:
        """
        Adds an EMA column to the DataFrame.

        Example:
            EMA.calculate(df, 20)
        """

        result = df.copy()

        result[f"EMA_{period}"] = (
            result[column]
            .ewm(span=period, adjust=False)
            .mean()
        )

        return result