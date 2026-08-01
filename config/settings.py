from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    # Application
    app_name: str
    app_env: str
    log_level: str

    # Database
    database_url: str

    # Interactive Brokers
    ib_host: str
    ib_port: int
    ib_client_id: int

    # OpenAI
    openai_api_key: str = ""

    # Trading
    use_paper_account: bool
    default_risk_percent: float
    max_position_percent: float
    max_daily_loss_percent: float

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()