# uvicorn app.use_jinja:app2 --reload
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

# 절대경로 지정을 위해 import
from pathlib import Path 

# Path(__file__).resolve() : 현재 파일 경로
# parent : 한 단계 상위폴더로 app 디렉터리가 됨
BASE_DIR = Path(__file__).resolve().parent

app2 = FastAPI()

# mount는 미들웨어, static 파일은 자바스크립트, png, jpg, css등. 일단 템플릿만 사용할거임
# app2.mount("/static", StaticFiles(directory="static"), name = "static")

# Jinja2Templates클래스에 대한 인스턴스(객체), template생성. 
# html파일을 서빙할건데, 이 html파일이 위치한곳 == template(dir)
template = Jinja2Templates(directory= BASE_DIR / "templates")


# reponse 타입을 json이 아니라 HTML로 서빙을 해주고 싶기때문에 이렇게 작성
# {"request": request, "id": id, "data": "helllo fastAPII"} 이 자리는 우리가 context라 부를거임
@app2.get("/items/{id}", response_class=HTMLResponse)
# (request: Request, id:str) request, id의 순서는 중요하지 않음 왜? type hinting을 했기 때문
async def read_item(request: Request, id:str):
    # request객체에는 어떤 정보가 담기는 지 확인
    print('request 객체 정보 : ' + str(request))
    print()
    # request의 속성값 알아보기
    print('request 속성값 : ' + str(dir(request)))
    print()
    # 요청하는 주체에 대한 헤더값 
    print('request 헤더 : ' + str(request["headers"]))
    # item.html에 id변수 전달
    return template.TemplateResponse("item.html", {"request": request, "id": id, "data": "helllo fastAPII"} )