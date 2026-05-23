from fastapi import FastAPI
import uvicorn

from Api.route import router

app = FastAPI()
app.include_router(router)
# 启动入口
if __name__ == "__main__":
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)