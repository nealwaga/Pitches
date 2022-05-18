import os

class Config:

    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = 'postgres://xrgdsogbbujwpn:d12f06661b2378f37bf632c5bdea88474c3b0e955f68f71708fd0d3f4eaf9702@ec2-52-71-69-66.compute-1.amazonaws.com:5432/d5bgskqdbseq5f'
    SECRET_KEY = '12345'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #Email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'neal.waga@student.moringaschool.com'
    MAIL_PASSWORD = 'WagaNealScrumhalf9.'
    SUBJECT_PREFIX = 'Pitch It Up!'
    SENDER_EMAIL = 'neal.waga@student.moringaschool.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri and uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    #rest of connection code using the connection string `uri`
    SQLALCHEMY_DATABASE_URI=uri


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'

class DevConfig(Config):
    '''
    Development configuration child class
    Args;
        Config: The parent configuration class with general configuration settings
    '''
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}