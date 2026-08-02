import pandas as pd

from app.indicators.sma import SMA


def test_sma():

    df = pd.DataFrame(
        {
            "Close": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        }
    )

    result = SMA.calculate(df, 5)

    assert "SMA_5" in result.columns
    assert len(result) == len(df)
    assert result["SMA_5"].iloc[-1] == 17.0