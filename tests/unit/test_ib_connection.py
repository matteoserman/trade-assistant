from app.services.broker.ibapi.broker import IBApiBroker


def test_connect_to_ib_gateway():

    broker = IBApiBroker()

    connected = broker.connect()

    assert connected is True

    assert broker.is_connected() is True

    broker.disconnect()