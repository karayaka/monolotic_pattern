import imp
from pydantic import BaseModel


class LoginModel(BaseModel):
    user_name:str
    password:str
    
class BaseUser(BaseModel):
    user_name:str    
    name:str
    surname:str

class UserCreate(BaseUser):
    password:str

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
    