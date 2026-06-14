from pydantic import BaseModel


class CommunicateMessageModel(BaseModel):
    role: str
    content: str

# 继承BaseModel 是Pydantic 模型
# 用来定义“数据结构 + 自动校验” 还能自动转 JSON
class FastApiBaseModel(BaseModel):
    code: int
    message: str
    data: object


class ChatRequest(BaseModel):
    message: str