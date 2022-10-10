from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core.config import get_db

router=APIRouter(
    prefix='/posts',
    tags=['Posts']    
)

@router.get('/')
def get_user(db:Session =Depends(get_db)):
    return 'Post'