from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "GET from root"


@app.post("/")
def root():
    return "POST from root"


@app.delete("/")
def root():
    return "POST from root"
