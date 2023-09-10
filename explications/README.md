# Chapitre 1 : les bases du web et HTTP 

## HTTP 

HTTP est un acronyme pour `Hyper Text Transfer Protocol`. 

HTTP est un protocole d'échange d'informations sur internet:
* ce protocole est sans état (stateless) : les requêtes sont
indépendantes
* c'est dans les réponses HTTP que peut se trouver le HTML
* il s'agit d'un protocole textuel (jusqu'à HTTP 2 en tous cas)
* il peut être chiffré pour éviter les modifications et "l'espionnag " par des tiers (le HTTPS)

## Parcours des requetes 

Un *client* va faire une *requete HTTP* et un *serveur* va lui répondre une *réponse HTTP*. 

TODO: insérer un schema

## Exemple de requete 

Nous allons nous focaliser sur HTTP en version 1. Dans cette version, les requêtes et réponses sont *uniquement* des échanges sous forme de texte. 

![Exemple de requete](images/exemple-reponse.jpg)
Source: [https://www.pierre-giraud.com/http-reseau-securite-cours/requete-reponse-session/]

HTTP étant un protocole, il est extrêment normé : il n'y a pas de place au hasard. Il doit également être très flexible pour permettre tout type d'échanges. 

Globalement toutes les requetes HTTP sont constituées 