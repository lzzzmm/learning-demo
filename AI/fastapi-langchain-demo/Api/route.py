from fastapi import APIRouter
from message import FastApiBaseModel, ChatRequest, CommunicateMessageModel
from aiService import deepSeekInvoke

router = APIRouter()
# 根路由
@router.get("/")
def read_root():
    obj =  FastApiBaseModel(code = 200, message = "success", data = None)
    return obj

@router.post("/user/llm")
def commmunication_with_llm(req: ChatRequest):
    message = CommunicateMessageModel(role="user", content=req.message)
    return deepSeekInvoke(message)