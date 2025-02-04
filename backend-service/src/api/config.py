import os

class Config:
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO').upper()
    COUNT_VALUE = os.getenv('COUNT_VALUE', 0)
    USER_NAME = os.getenv('USER_NAME', 'default')