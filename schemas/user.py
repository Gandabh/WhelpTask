from pydantic import BaseModel
import dotenv
import os


dotenv.load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


class User(BaseModel):
    age: int
    name: str
    surname: str
    username: str
    email: str
    gender: str
    password: str


    class Config:
        show_extra = {
            "example": {
                "age": "21",
                "name": "Gandab",
                "surname": "Hasanova",
                "username": "Gandab123",
                "email": "gandab@gmail.com",
                "gender": "F",
                "password": "Gandab123"
            }
        }


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Gandab123",
                "password": "Gandab123"
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str = SECRET_KEY