from fastapi.security import  HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
import dotenv
import os


dotenv.load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


class AuthHandler():
    security = HTTPBearer()
    pwd_context =CryptContext(schemes=['bcrypt'], deprecated="auto")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):

        return self.pwd_context.verify(plain_password, hashed_password)
