import os

class Config:
    APP_NAME = "DevSecOps Demo App"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False") == "True"