import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'CHANGEME'
    # Flask-WTF variable
    CSRF_ENABLED = True
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    # DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    # DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
