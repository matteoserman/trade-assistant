import pandas as pd

from app.indicators.atr import ATR


def test_atr():

    df = pd.DataFrame(
        {
            "High": [11, 12, 13, 14, 15],
            "Low": [9, 10, 11, 12, 13],
            "Close": [10, 11, 12, 13, 14],
        }
    )

    result = ATR.calculate(df, 3)

    assert "ATR_3" in result.columns
    assert len(result) == len(df)