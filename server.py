# app을 실행시켜줄거임
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.project:app3", host="localhost", port=8000, reload=True)