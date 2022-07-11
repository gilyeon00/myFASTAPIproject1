# app을 실행시켜줄거임
import uvicorn

# terminal에 uvicorn app.03_fastapi~~ 치는거 귀찮으니까, 'python server.py' 입력하면 서버 구동되게끔 
if __name__ == "__main__":
    uvicorn.run("app.03_fastapi_project:app3", host="localhost", port=8000, reload=True)