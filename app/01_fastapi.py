# 공식문서 : https://fastapi.tiangolo.com/ko/
# 자동 대화형 API 문서 :  http://127.0.0.1:8000/docs
# pydantic은 dto 인듯 

# typing이란 문법
from typing import Optional

# fastapi라이브러리에서 FastAPI클래스 import
from fastapi import FastAPI

# app1은 FastAPI클래스의 인스턴스
app1 = FastAPI()

# @는 '데코레이트 문법' get()메서드로 함수를 꾸며준다 생각하면 될듯
# 이 뭉텅이 하나하나를 라우터라 함 
# 우리가 하는 과정은 app1인스턴스 안에 이 라우터들을 정의한거임
# uvicorn으로 실행을 했을때, url에 대해서 요청을하면 인스턴스의 라우터를 하나하나 찾아가서 해당 로직 수행 return으로 응답
#http://127.0.0.1:8000
@app1.get("/")
def read_root():
    print("My first FastAPI app")
    return {"Hello~~~" : "World"}

#http://127.0.0.1:8000/hello
@app1.get("/hello")
def read_fastapi_hello():
    return {"Hello" : "fastapii"}

# {item_id} -> 동적 라우팅
# http://127.0.0.1:8000/items -> 아무것도 안뜸
# http://127.0.0.1:8000/items/123 -> {item_id} 자리에 123들어감
#                                {"item_id":123,"q":null}
# q는 쿼리, Optional은 말그대로 있어도 없어도 상관없음. 여기서 디폴트==none
# http://127.0.0.1:8000/items/123?q=hello ->  {"item_id":123,"q":"hello"}
@app1.get("/items/{item_id}")
def read_item(item_id: int, q : Optional[str] = None) :
    return {"item_id" : item_id, "q" : q}

#http://127.0.0.1:8000/items/123/rlfdus?q=helloooooo   ->    {"item_id":123,"q":"helloooooo","xyz":"rlfdus"}
@app1.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q : Optional[str] = None) :       
    return {"item_id" : item_id, "q" : q, "xyz": xyz }


