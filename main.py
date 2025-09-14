from fastapi import FastAPI

app = FastAPI(title="Sample FastAPI", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI 🚀"}

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "pong"}