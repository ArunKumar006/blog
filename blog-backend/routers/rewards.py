from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
import database,schemas,models
from repository import rewards
router=APIRouter(tags=["Rewards"])

@router.get('/list')
def reward(db:Session=Depends(database.get_db)):
    blogs= rewards.get_all(db)
    return blogs