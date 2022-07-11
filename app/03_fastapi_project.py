# uvicorn app.use_jinja:app2 --reload
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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