from pydantic import BaseModel

class BasePost(BaseModel):
    id:int
    title:str
    content:str

class PostCreate(BaseModel):
    pass

class PostList(BasePost):
    user_name_surname:str
    comments_count:int
    
