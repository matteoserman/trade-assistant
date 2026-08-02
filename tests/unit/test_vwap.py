import pandas as pd

from app.indicators.vwap import VWAP


def test_vwap():

    df = pd.DataFrame(
        {
            "High": [11, 12, 13],
            "Low": [9, 10, 11],
            "Close": [10, 11, 12],
            "Volume": [100, 200, 300],
        }
    )

    result = VWAP.calculate(df)

    assert "VWAP" in result.columns

    assert len(result) == 3

    assert result["VWAP"].iloc[-1] > 0