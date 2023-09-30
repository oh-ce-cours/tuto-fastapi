# Chapitre 3 : premiers pas avec fastapi 
## Installation 

Nous avons rajouté fasapi aux dépendances du projet : `pip install -r requirements.txt`

Parmis les dépendances notable de `fastapi`, nous pouvons noter : 
* `starlette` : un framework HTTP asynchrone 
* `pydantic` : un outil de validation / sérialisation / désérialisation de données 

En effet, `fastapi` se base sur `starlette` tout en permettant de gérer facilement des validations de données grâce à `Pydantic` qui est intégré facilement. [Plus d'informations ici](https://fastapi.tiangolo.com/fr/alternatives/#:~:text=Starlette%20fournit%20toutes%20les%20fonctionnalit%C3%A9s,Python%20(en%20utilisant%20Pydantic)).


Nous verrons tout cela dans le chapitre suivant, pour l'instant, nous allons nous faire nos premiers pas avec `fastapi`. 

## Ma première route 

Globalement, quand vous développez dans un langage de haut niveau une application web, vous n'avez pas besoin de vous occuper du HTTP (au moins dans un premier temps). C'est le framework qui va l'abstraire pour vous. 

Tout ce qui doit vous inquiéter c'est : *qu'est-ce que je dois faire lorsqu'un utilisateur appelle une certaine URL ?!*. Vous verrez que déjà répondre à cette question n'est pas forcément évident :) 

`fastapi` vous permet de facilement lier un motif d'*url* à une fonction python, en utilisant un décorateur. Comment un décorateur fonctionne sort du cadre de ce cours, sachez que c'est le `@` que l'on verra dans les codes. Plusieurs frameworks python font cela (`flask` par example).

Tout les codes que nous verrons sont inspirés du [tutoriel officiel de fastapi](https://fastapi.tiangolo.com/fr/tutorial/first-steps/). 

Voilà comment cela fonctionne. Nous avons créé le fichier suivant dans le dossier `codes/main.py`

```python 
from fastapi import FastAPI # on importe fastapi

app = FastAPI() # on créé une application 


@app.get("/") # le fameux décorateur liant la fonction "root" à l'url "/"
def root():
    return {"message": "Hello World"} # ce qui sera retourné quand on appelle l'endpoint "/" 
```

Ce code permet de réagir aux requetes `GET` effectuée sur l'url racine : `/` 

Pour le lancer il suffit de lancer la commande suivante dans un terminal situé dans le dossier `codes` : `uvicorn main:app --reload` 

* `uvicorn` est le serveur web qui nous allons utiliser pour gérer les requetes 
* `main:app` indique de charger la variable `app` du fichier `main.py` situé dans le dossier courant
* `--reload` indique de redémarrer automatiquement le serveur quand il détecte que le contenu du fichier `main.py` a changé 


Cela affichera les lignes suivantes : 
```shell 
(tuto-fastapi) ➜  codes git:(3-fastapi-premiers-pas) ✗ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['***/tuto-fastapi/codes']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12519] using StatReload
INFO:     Started server process [12521]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Le serveur est maintenant lancé, il attend les requêtes. Nous pouvons lui en faire :  
* accédez à l'url avec votre navigateur : `http://127.0.0.1:8000/`
* (exercice pour le lecteur) : effectuer la requête avec `curl` ou en python avec `request` 


PS: pour ceux qui se posent la question, contrairement au tutoriel, je n'utilise pas `async def` pour définir mes fonctions, pour ne pas vous embrouiller avec l'asynchrone. Pour plus d'informations, regardez [la partie expliquant l'asynchrone sur le site de fastapi](https://fastapi.tiangolo.com/fr/async/#vous-etes-presses). 


## Créer plusieurs routes 

Pour créer plusieurs routes, il suffit de les déclarer en utilisant le décorateur de fastapi. 

Vous pouvez voir cela en pratique dans le fichier `codes/plusieurs_routes.py`. 

Pour voir si vous avez bien compris posez vous les questions suivantes : 
1. comment lancer `uvicorn` pour qu'il utilise cette application ? 
1. quelles sont les routes exposées ? 
1. comment est géré le routage / l'ordre de priorité sur les routes ?
1. que se passe-t-il si j'accède à une route qui n'existe pas ? 
1. que se passe-t-il si je modifie une des routes pour intégrer une erreur côté serveur (par exemple `1/0`) ?

<details>
  <summary>Réponses</summary>
  
  1. `uvicorn plusieurs_routes:ma_super_application --reload`
  1. `/date`, `/time` et `/datetime` 
  1. actuellement, comme nos routes sont en dur, `fastapi` va détecter correctement nos différentes routes. Si une partie de l'url était variable (nous verrons dans le chapitre suivant comment faire), on pourra se poser des questions. 
  1. `fastapi` retourne une 404 car l'URL n'existe pas. Note: notre code n'a jamais été appelé, c'est `fastapi` qui gère ça tout seul 
  1. `fastapi` retourne une 500 car le code crash coté serveur : toutes les exceptions qui arrivent au framework vont générer des erreurs 500 (on peut retrouver les exceptions et la stacktrace dans le terminal)

</details>


## Gérer les différents verbes HTTP 

Pour voir comment réagir à différents verbes, allez voir le fichier `codes/plusieurs_fichiers.py`. 

Pour voir si vous avez bien compris posez vous les questions suivantes : 
1. quels sont les verbes disponibles ? 
1. comment faire pour appeler les différentes fonctions ? 
1. que se passe-t-il lorsque l'on demande un verbe non implémenté dans le code (par exemple `patch` dans le fichier d'exemple) ? 

<details>
  <summary>Réponses</summary>
  
  1. `.get`, `.post`, `.delete`, `.put`, `.patch`, c'est à dire les différents verbes HTTP
  1. on va utiliser `curl` ou `requests` pour faire les requêtes, un navigateur ne permet de n'effectuer simplement (sans coder) que des requetes GET
    * pour get: `curl -X GET localhost:8000`
    * pour post: `curl -X POST localhost:8000`
    * pour delete: `curl -X DELETE localhost:8000`
  1. `fastapi` le gère pour nous, en renvoyant une erreur `405` (Method Not Allowed)

</details>

## Conclusion 

Nous venons de voir les bases de `fastapi` pour créer notre première API. 

Le framework gère toute la machinerie HTTP pour nous, afin que nous puissions nous concentrer sur le code métier.

L'API est actuellement assez peu dynamique car : 
* elle ne réagit qu'à des URLs écrites en dur 
* n'accepte pas de paramètres

Nous verrons comment répondre à ces deux problèmes dans le chapitre suivant. Évidemment `fastapi` va nous simplifier la vie. 

Pour accéder au prochain chapitre: `git switch 4-fastapi-parametres`