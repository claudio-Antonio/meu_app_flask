import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "minha-chave-secreta-de-demo-mudar-depois")
    SQLALCHEMY_DATABASE_URI = "sqlite:///usuarios.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
