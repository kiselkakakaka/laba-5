from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Лабораторная 5 — FastAPI работает через Docker и Nginx!"}
