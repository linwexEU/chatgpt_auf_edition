from datetime import datetime, timedelta 
from passlib.context import CryptContext 
from jose import jwt 

from config import settings 
from app.users.dao import UsersDAO


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str): 
    return pwd_context.hash(password) 

def verify_password(hashed_password, plain_password): 
    return pwd_context.verify(hashed_password, plain_password) 


def create_access_token(data: dict) -> str: 
    to_encode = data.copy() 
    expire = datetime.utcnow() + timedelta(days=14) 
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITH
    )
    return encoded_jwt 


async def authenticate_user(username: str, password: str): 
    user = await UsersDAO.find_one_or_none(username=username)
    if user and verify_password(password, user["Users"].hashed_password): 
        return user 
    return None