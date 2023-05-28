from src.config.env import config_env
from src.config.logger import config_logger


def config():
    config_env()
    config_logger()
