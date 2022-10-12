from jose import JWTError, jwt
from schemas.users import TokenData
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("user_name")
        if email is None:
            raise credentials_exception
        token_data = TokenData(
            user_name=email,
            id=payload.get("id"),
            name=payload.get("name"),
            surname=payload.get("surname")
            )
        return token_data
    except JWTError:
        raise credentials_exception


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token,credentials_exception)