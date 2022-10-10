from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.repositorys.user_repository import create_user_new
from schemas.users import UserCreate
from core.config import get_db

router=APIRouter(
    prefix='/users',
    tags=['Users']    
)

@router.get('/')
def get_user(db:Session =Depends(get_db)):
    return 'users'

@router.post('/')
def create_user(user:UserCreate,db:Session =Depends(get_db)):
    usr= create_user_new(db,user)   
    return usr.id

@router.post('/login')
def login():
    
    pass

