from pydantic_settings import BaseSettings 
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings): 
    API_KEY: str 

    SECRET_KEY: str
    ALGORITH: str

    DB_HOST: str 
    DB_PORT: int 
    DB_USER: str 
    DB_PASS: str 
    DB_NAME: str

    @property 
    def DATABASE_URL(self): 
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    class ConfigDict: 
        env_file = ".env"


settings = Settings() 

