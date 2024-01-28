from fastapi import APIRouter, Response, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from app.users.schemas import SAuth 
from app.users.auth import authenticate_user, create_access_token, get_password_hash 
from app.users.dao import UsersDAO



router = APIRouter(
    prefix="/auth",
    tags=["Auth & Reg"]
)


@router.post("/registration")
async def reg_user(data: SAuth): 
    user = await UsersDAO.find_one_or_none(username=data.username) 
    if user: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    hashed_password = get_password_hash(data.password) 
    await UsersDAO.add(username=data.username, hashed_password=hashed_password, last_query="", last_answer="")
    return {"message": "Done!"}


@router.post("/login")
async def login_user(response: Response, data: SAuth): 
    user = await authenticate_user(data.username, data.password) 
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) 
    access_token = create_access_token({"sub": str(user["Users"].user_id)})
    response.set_cookie("auth_access", access_token)
    return {"access_token": access_token}










