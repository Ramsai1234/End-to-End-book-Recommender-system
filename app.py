from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
import sys


#logging.info("starting the application...")
try:
    a=1/0
except Exception as e:
    raise AppException(e,sys)