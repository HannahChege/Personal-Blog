import os

class Config:

    
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:password@localhost/blog'
    DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:password@localhost/blog_test'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}