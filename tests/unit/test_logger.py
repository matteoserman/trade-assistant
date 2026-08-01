from app.utils.logger import get_logger


def test_logger():
    logger = get_logger("trade_assistant")

    logger.info("Logger is working!")

    assert logger.name == "trade_assistant"