from app.domain.account import AccountSummary


def test_account_summary_defaults():

    account = AccountSummary()

    assert account.account_id == ""
    assert account.net_liquidation == 0.0
    assert account.buying_power == 0.0
    assert account.cash_balance == 0.0
    assert account.currency == "USD"