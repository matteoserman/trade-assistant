import pandas as pd

from app.indicators.ema import EMA


def test_ema():

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

    result = EMA.calculate(df, 3)

    assert "EMA_3" in result.columns

    assert len(result) == len(df)

    assert not result["EMA_3"].isna().all()