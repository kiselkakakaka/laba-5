from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Lab 5 — Продакшн и Docker работает!"}
