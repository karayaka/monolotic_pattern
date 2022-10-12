from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from core.hashing import Hasher
from db.repositorys.user_repository import create_user_new, get_user_by_username,get_users
from schemas.users import UserCreate,LoginModel,LoginResponseModel
from core.config import get_db
from core.JWTtoken import create_access_token

router=APIRouter(
    prefix='/users',
    tags=['Users']    
)

@router.get('/')
def get_user(db:Session =Depends(get_db)):
    return get_users(db)

@router.post('/')
def create_user(user:UserCreate,db:Session =Depends(get_db)):
    usr= create_user_new(db,user)   
    return usr.id

@router.post('/login',response_model=LoginResponseModel)
def login(login:LoginModel,db:Session =Depends(get_db)):
    usr=get_user_by_username(db,login.user_name)
    if not usr:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password or username")
    elif not Hasher.verify_password(login.password,usr.password_hass):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password or username")
    access_token = create_access_token(data={
            "user_name": usr.user_name,
            "name":usr.name,
            "surname":usr.surname,
            "id":usr.id
            })
    return LoginResponseModel(token=access_token,token_type='bearer')

