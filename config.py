import os

class Config:

    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = 'postgres://ydpppvnrrwcyir:cfabd1313da50a2a7610121112763b7212a866fc68a41f5c5d773371434741e2@ec2-34-201-95-176.compute-1.amazonaws.com:5432/dfdnkqfol0f6ag'
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