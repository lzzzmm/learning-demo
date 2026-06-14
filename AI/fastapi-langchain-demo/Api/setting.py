from functools import lru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEEPSEEK_API_KEY:str = "unknow"
    class Config:
        env_file = ".env.dev"   # 自动读取 .env


# 函数结果缓存装饰器
@lru_cache
def get_settings():
    return Settings()