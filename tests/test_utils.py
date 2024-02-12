import logging
from src.utils import setup_logging

def test_setup_logging():
    """
    Test the setup_logging function to ensure it correctly configures and returns a logger.
    """
    logger_name = 'test_logger'
    logger = setup_logging(logger_name)
    
    # Verify the logger has the correct name
    assert logger.name == logger_name
    
    # Verify the logger's level is set to INFO (default)
    assert logger.level == logging.INFO

