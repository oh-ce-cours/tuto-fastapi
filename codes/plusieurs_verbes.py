from fastapi import FastAPI

app = FastAPI()
# on peut définir le verbe en choisissant la méthode
# de "app" que l'on appelle (get, post, delete)


@app.get("/")
def root():
    return "GET from root"


@app.post("/")
def root():
    return "POST from root"


@app.delete("/")
def root():
    return "DELETE from root"


# Note: l'exemple suivant n'a pour but que de montrer
# comment appeler les différents verbes. En pratique
# vous voudrez effectuer des actions en lien avec le
# verbe HTTP demandé.
