from sqlalchemy import select, insert
from database import async_session_maker 


class BaseDAO: 
    model = None

    @classmethod 
    async def get_all(cls): 
        async with async_session_maker() as session: 
            query = select("*").select_from(cls.model)
            result = await session.execute(query) 
            return result.mappings().all()

    @classmethod 
    async def find_one_or_none(cls, **filter_data): 
        async with async_session_maker() as session: 
            query = select(cls.model).filter_by(**filter_data)
            result = await session.execute(query) 
            return result.mappings().one_or_none()
        
    @classmethod 
    async def add(cls, **data): 
        async with async_session_maker() as session: 
            query = insert(cls.model).values(**data) 
            await session.execute(query) 
            await session.commit() 