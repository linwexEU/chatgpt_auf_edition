from fastapi import APIRouter, Depends, BackgroundTasks
from app.api.bingai import ChatGPT
from app.api.schemas import AufData
from app.styles.dao import StylesDAO
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.schemas import User 


router = APIRouter(
    prefix="/gpt",
    tags=["ChatGptAuf"]
)


async def get_answer_from_gpt(style, query, user): 
    style = await StylesDAO.get_style(style)
    if style is None: 
        style = ""
    
    answer = ChatGPT.get_answer(style + query)   
    await UsersDAO.add_answer(user["Users"].user_id, query, answer)

@router.post("/gpt_answer")
async def get_answer_from_task(background_tasks: BackgroundTasks, data: AufData, current_user: User = Depends(get_current_user)): 
    background_tasks.add_task(get_answer_from_gpt, data.style.split("-")[0].strip(), data.query, current_user)
















