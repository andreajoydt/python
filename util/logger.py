import logging
from logging import Logger as PythonLogger
from functools import wraps

class Logger:

    def __init__(self):
        self.__logger = logging.getLogger("MyApp")
        formater = '%(asctime)s - %(name)s - %(filename)s - %(message)s'
        logging.basicConfig(filename="my_app.log", level=logging.DEBUG, format=formater)
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            print("Simple pero elepante")
        return cls.instance
    
    def get_logger(self) -> PythonLogger:
        return self.__logger

    def enable_logging(func):
        def wrapper(*args, **kwargs):
            Logger().get_logger().info()
            logger.info(f"Begin: ")