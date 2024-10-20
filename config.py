import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'md0WJsjaOOuf1T')


