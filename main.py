from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "안녕하세요, when2meet 앱입니다!"}