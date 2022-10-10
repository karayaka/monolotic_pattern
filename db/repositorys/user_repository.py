from unicodedata import name

from sqlalchemy import null
from schemas.users import UserCreate
from sqlalchemy.orm import Session
from ..models.user import User
from core.hashing import Hasher



def create_user_new(db:Session, user:UserCreate):
    usr=User(
        user_name=user.user_name,
        password_hass=Hasher.get_password_hash(user.password),
        name=user.name,
        surname=user.surname
    )
    db.add(usr)
    db.commit()
    db.refresh(usr)
    return usr

def get_user_by_username(db:Session,user_name:str):
    user= db.query(User).filter(User.user_name==user_name).first()
    if user:
        return user
    return null


