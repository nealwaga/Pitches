import os

class Config:

    #Location of the database with authentication 
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = 'postgres://amkzcodphgpjma:02e66eaaa6a49b0de4994d216778e624bfe3059ff15cf7d5e1a756c3726da2de@ec2-52-71-69-66.compute-1.amazonaws.com:5432/df4s8d2jutk2v9'
    SECRET_KEY = 'S9WnSR256m52VgJTzgAv5AqfQXewgQ'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #Email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch It Up!'
    SENDER_EMAIL = 'neal.waga@student.moringaschool.com'
    #MAIL_PASSWORD = 'WagaNealScrumhalf9.'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #pass
    # uri = os.getenv("DATABASE_URL")  # or other relevant config var
    # if uri.startswith("postgres://"):
    #     uri = uri.replace("postgres://", "postgresql://", 1)

    #     SQLALCHEMY_DATABASE_URI=uri
    #SQLALCHEMY_DATABASE_URI = 'postgres://micofbevbarmcb:e4efc3603b23e6b8e239f63906a9cb9c6653f69a567e32cb65667bbd9f16da90@ec2-52-200-215-149.compute-1.amazonaws.com:5432/de2jdr1js7qf1k'
    #SQLALCHEMY_DATABASE_URI = 'postgres://tafjcklyafymbr:47172dc527f27fbe13c1c8ff60b4ed057ea2f89dadd4741ffd2a57d779ac7075@ec2-54-165-184-219.compute-1.amazonaws.com:5432/dfmfmae5bn6h7'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'
    pass 

class DevConfig(Config):
    '''
    Development configuration child class
    Args;
        Config: The parent configuration class with general configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/pitch'
    

DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}