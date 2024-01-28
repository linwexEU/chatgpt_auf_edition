from fastapi import Request, Depends, HTTPException, status
from jose import JWTError, jwt 
from config import settings 
from datetime import datetime 

from app.users.dao import UsersDAO 


def get_token(request: Request): 
    token = request.cookies.get("auth_access")
    if not token: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) 
    return token 

async def get_current_user(token: str = Depends(get_token)): 
    try: 
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITH
        )
    except JWTError: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)  
    expire: str = payload.get("exp") 
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get("sub")
    if not user_id: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) 
    user = await UsersDAO.find_one_or_none(user_id=int(user_id))
    if not user: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) 
    return user






