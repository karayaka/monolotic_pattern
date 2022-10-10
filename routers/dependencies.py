from routers import route_item
from . import route_user,route_post

def include_router(app):  
    app.include_router(route_user.router)
    app.include_router(route_post.router)
    app.include_router(route_item.router)