from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

# Bloco de carrega de aariáveis de Ambiente
load_dotenv(override=True)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

#  Inicialização do FastAPI
app = FastAPI()

# Criação de variável de criptografia
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")