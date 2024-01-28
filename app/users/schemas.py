from pydantic import BaseModel


class SAuth(BaseModel): 
    username: str 
    password: str 

class User(BaseModel):
    user_id: int
    username: str 
    hashed_password: str