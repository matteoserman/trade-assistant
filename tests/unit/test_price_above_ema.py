import pandas as pd

from app.indicators.ema import EMA
from app.services.scanner.rules.ema import PriceAboveEMA
from app.services.scanner.scanner import Scanner


class FakeMarketService:

    def get_history(
        self,
        symbol,
        timeframe="1 day",
        lookback="1 Y",
    ):

        df = pd.DataFrame(
            {
                "Close": [
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                ]
            }
        )

        return EMA.calculate(df, 5)


def test_price_above_ema():

    market = FakeMarketService()

    scanner = Scanner(market)

    scanner.add_rule(
        PriceAboveEMA(5)
    )

    results = scanner.scan_watchlist(
        ["AAPL", "MSFT"]
    )

    assert len(results) == 2

    assert results[0].passed

    assert results[0].score == 100.0