from datetime import datetime, timedelta
from schemas.users import TokenData
from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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