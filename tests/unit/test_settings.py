from config.settings import settings


def test_settings_loaded():
    assert settings.app_name == "Trade Assistant"
    assert settings.ib_host == "127.0.0.1"
    assert settings.ib_port == 4002
    assert settings.use_paper_account is True