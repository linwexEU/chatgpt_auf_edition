from pydantic import BaseModel 

class AufData(BaseModel): 
    query: str 
    style: str