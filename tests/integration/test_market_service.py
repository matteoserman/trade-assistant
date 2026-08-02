from app.services.broker.ibapi.broker import IBApiBroker
from app.services.market.service import MarketService


def test_market_service():

    broker = IBApiBroker()

    assert broker.connect()

    market = MarketService(broker)

    df = market.get_history(
        symbol="AAPL",
        timeframe="1 day",
        lookback="1 Y",
    )

    assert not df.empty

    print(df.head())
    print()
    print(df.tail())

    broker.disconnect()