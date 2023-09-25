from fastapi import FastAPI  # on importe fastapi

app = FastAPI()  # on créé une application


@app.get("/")  # le fameux décorateur liant la fonction "root" à l'url "/"
def root():
    return {"message": "Hello World"}  # ce qui sera retourné quand on appelle l'endpoint "/"
