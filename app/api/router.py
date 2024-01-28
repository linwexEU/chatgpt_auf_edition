from fastapi import APIRouter, Depends
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


@router.post("/get_answer_from_gpt")
async def get_answer_from_gpt(data: AufData, current_user: User = Depends(get_current_user)): 
    style = await StylesDAO.get_style(data.style.split("-")[0].strip())
    if style is None: 
        style = ""
    
    answer = ChatGPT.get_answer(style + data.query) 
    
    await UsersDAO.add_answer(current_user["Users"].user_id, data.query, answer)

    return {"message": answer}
    


















