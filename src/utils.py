import logging

def setup_logging(name):
    """
    Sets up logging with the given name and returns the logger.

    Args:
        name (str): The name of the logger.

    Returns:
        Logger: The configured logger.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(name)
