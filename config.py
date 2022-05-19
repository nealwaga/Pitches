import os

class Config:

    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:1234@localhost/pitchie'
    SQLALCHEMY_DATABASE_URI = 'postgresql://jtmraqtapxqdvn:d30b6ac1820f573a3ff4cfa076781c9ccec6bb562ce6f76ef14d7983f9402ade@ec2-34-231-177-125.compute-1.amazonaws.com:5432/d8e8kap901j6ve'
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:1234@localhost/pitchie'
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri and uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    #rest of connection code using the connection string `uri`
    SQLALCHEMY_DATABASE_URI=uri


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:1234@localhost/pitchie'

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