import requests 
import pprint

# requete GET vers le listing d'utilisateurs
print("Récupération d'une liste d'utilisateurs")
response = requests.get("https://reqres.in/api/users?page=1")
print(response.json())

## on peut passer les paramètres dans un dictionnaire (plus pratique)
print("Récupération d'un utilisateur (2eme version)")
params = {"page": 1}
response = requests.get("https://reqres.in/api/users", params=params)
print(response.json())


# création d'un utilisateur 
print("Création d'un utilisateur")
data = {"name": "John Doe","job": "Researcher"}
response = requests.post("https://reqres.in/api/users", data=data)
print(response.status_code)
print(response.json())


# Mise à jour d'un utilisateur 
print("Mise à jour d'un utilisateur")
data = {"first_name": "Matthieu"}
response = requests.put("https://reqres.in/api/users/2023", data=data)
print(response.status_code)

# Equivalent de jq
## nous pouvons récupérer les emails des utilisateurs dans 
## une variable il s'agit d'un dictionnaire classique
print("équivalent de jq -- récupération des emails")
response = requests.get("https://reqres.in/api/users?page=1")
for user in response.json()["data"]:
    print(user["email"])
