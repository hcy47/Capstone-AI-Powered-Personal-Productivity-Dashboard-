import os

class DevelopmentConfig():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = True
    SECRET_KEY = 'super secret secrets'

class ProductionConfig():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change_this_in_production')