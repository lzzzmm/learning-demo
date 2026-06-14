from fastapi import FastAPI
import uvicorn
from route import router

# 创建 FastAPI 应用 app = 整个网站系统
app = FastAPI()
# 把 route.py 里的接口“挂载”进来  把 route.py 里的所有接口，加入到这个 app 里
app.include_router(router)
# 启动入口
# reload=True 开发模式 代码改了会自动重启服务器
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)