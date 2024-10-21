import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'md0WJsjaOOuf1T'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    
# Je kunt ook een configuratieklasse gebruiken als je meer omgevingen hebt, zoals DevelopmentConfig of ProductionConfig.
