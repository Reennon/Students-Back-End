from flask import Config

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLE =True
    ASERT_DEBUG = True
    CACHE_TYPE = 'simple'