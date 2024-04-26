from fastapi import FastAPI,Response
from database import engine,Base
import models
from routers import user,blog,authentication,rewards
app = FastAPI()
models.Base.metadata.create_all(engine)

# @app.route("/")
# def home(request):
#     return Response("hello")


app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentication.router)
app.include_router(rewards.router)