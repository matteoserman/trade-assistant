from app.services.broker.ibapi.broker import IBApiBroker


def test_ib_account_and_positions():

    broker = IBApiBroker()

    assert broker.connect()

    account = broker.get_account_summary()

    assert account is not None
    assert account.account_id != ""

    print()
    print(account)

    positions = broker.get_positions()

    print()
    print("POSITIONS")
    print("------------------------")

    for position in positions:
        print(position)

    broker.disconnect()