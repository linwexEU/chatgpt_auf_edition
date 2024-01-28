from app.dao.base import BaseDAO  
from app.users.models import Users
from database import async_session_maker
from sqlalchemy import update, select


class UsersDAO(BaseDAO): 
    model = Users 

    @classmethod 
    async def add_answer(cls, user_id, last_query, last_answer): 
        async with async_session_maker() as session: 
            query = (
                update(cls.model)
                .where(cls.model.user_id == user_id)
                .values(last_answer=last_answer, last_query=last_query)
            )
            await session.execute(query) 
            await session.commit() 

    @classmethod 
    async def get_user(cls, user_id): 
        async with async_session_maker() as session:
            query = (
                select("*")
                .select_from(cls.model)
                .where(cls.model.user_id == user_id)
            ) 
            result = await session.execute(query) 
            return result.mappings().all() 