# uvicorn app.use_jinja:app2 --reload
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import mongodb

# 절대경로 지정을 위해 import
from pathlib import Path 

# Path(__file__).resolve() : 현재 파일 경로
# parent : 한 단계 상위폴더로 app 디렉터리가 됨
BASE_DIR = Path(__file__).resolve().parent

app3 = FastAPI()

template = Jinja2Templates(directory= BASE_DIR / "templates")


@app3.get("/", response_class=HTMLResponse)
async def root(request: Request):

    return template.TemplateResponse("index.html", {"request": request, "title":'콜렉터 북북이'} )


@app3.get("/search", response_class=HTMLResponse)
async def search(request: Request, q:str):
    print(q)
    return template.TemplateResponse("index.html", {"request": request, "title":'콜렉터 북북이', "keyword":q} )


#from motor.motor_asyncio import AsyncIOMotorClient
#from odmantic import AIOEngine

#from config  import MONGO_DB_NAME,MONGO_URL
# 참고 https://art049.github.io/odmantic/engine/ engine코드 붙이고, MONGO_URL로 대치
# 서버 구동될때 DB연결 startup 이벤트 생성
@app3.on_event("startup")
async def on_app_start():
    print("hellooo serverrrrr")
    #여기에다가 작성하면 스코프 문제가 있어서 다른 라우터 사용할 때 작동안됨
    #client = AsyncIOMotorClient(MONGO_URL)
    #engine = AIOEngine(motor_client=client, database=MONGO_DB_NAME)
    mongodb.connect()

# 서버꺼지면 구동되는 이벤트
@app3.on_event("shutdown")
async def on_app_shutdown():
    pass