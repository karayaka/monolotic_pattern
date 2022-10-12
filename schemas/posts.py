from xml.sax.xmlreader import InputSource
from pydantic import BaseModel
from schemas.users import UserCreate


class BasePost(BaseModel):
    title:str
    content:str

class PostCreate(BasePost):
    pass

class PostList(BasePost):
    id:int
    user_name_surname:str
    comments_count:int
    
