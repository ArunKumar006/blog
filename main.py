from fastapi import FastAPI,Response
from database import engine,Base
import models
from routers import user,blog
app = FastAPI()
models.Base.metadata.create_all(engine)

# @app.route("/")
# def home(request):
#     return Response("hello")


app.include_router(user.router)