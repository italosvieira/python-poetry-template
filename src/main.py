import logging

from src.config import config


def main():
    config()
    logging.info("Info")
    logging.debug("Debug")
    logging.warning("Warning")
    logging.error("Error")


if __name__ == "__main__":
    main()
