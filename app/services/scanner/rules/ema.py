import pandas as pd

from app.services.scanner.rules.base import Rule


class PriceAboveEMA(Rule):
    """
    Passes when the latest closing price is above the specified EMA.
    """

    def __init__(self, period: int):
        self.period = period

    @property
    def name(self) -> str:
        return f"Price Above EMA {self.period}"

    def evaluate(self, df: pd.DataFrame) -> bool:

        column = f"EMA_{self.period}"

        if column not in df.columns:
            raise ValueError(
                f"EMA column '{column}' not found."
            )

        return bool(
            df["Close"].iloc[-1]
            >
            df[column].iloc[-1]
        )