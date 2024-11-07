import logging

def setup_logger():
    # Create a logger
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)  # Set the default level to DEBUG
    
    # Create a file handler for logging to a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)  # Log DEBUG and above to the file
    
    # Create a stream handler to log to console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)  # Log INFO and above to the console
    
    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger
