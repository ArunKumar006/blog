from sqlalchemy.orm import Session
import models
from fastapi import HTTPException,status

def get_all(db:Session):
    blogs= db.query(models.Rewards).all()
    print(blogs)
    return blogs


