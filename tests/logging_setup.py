import logging


def setup_logger():
    # Set up logging
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        handlers=[logging.StreamHandler()])