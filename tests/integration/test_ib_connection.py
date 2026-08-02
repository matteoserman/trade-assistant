from app.services.broker.ibapi.broker import IBApiBroker


def test_ib_broker():

    broker = IBApiBroker()

    assert broker.connect()

    account = broker.get_account_summary()

    assert account is not None

    bars = broker.get_historical_data(
        symbol="AAPL",
        duration="1 Y",
        bar_size="1 day",
    )

    assert len(bars) > 200

    print()
    print(bars[0])
    print("...")
    print(bars[-1])

    broker.disconnect()