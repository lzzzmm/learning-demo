import code
from hashlib import new

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

router = APIRouter()
# 根路由
@router.get("/")
def read_root():
    obj =  FastApiBaseModel(code = 200, message = "success", data = None)
    return obj



class FastApiBaseModel(BaseModel):
    code: int
    message: str
    data: object