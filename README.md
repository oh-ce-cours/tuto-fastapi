# Tutoriel Fastapi 

## Concept 

Ce dépot contient un tutoriel présentant le framework web fastapi. Il est a destination de data engineers, non spécialisés en développement backend ou web. 

Le tutoriel possède les chapitres suivants : 

1. explications de l'HTTP, des verbes HTTP et de l'intérêt d'un framework web 
1. comment automatiser des requêtes webs en ligne de commande (curl / requests)
1. première utilisation de fastapi et réaction aux événements 
1. Pydantic et la validation des paramètres passés aux routes 
1. Projet de mise en situation : simuler et analyser des données de caisses de supermarché
    * généreration de fausses données avec faker
    * définition de l'architecture globale 
    * manipulation de données en SQL 

## Hors programme 

Nous ne traiterons pas les sujets suivants pour ne pas diluer le message principal : 

* authentification / autorisation des utilisateurs 
* manipulations de données à travers un ORM 

## Organisation 

Le tutoriel est découpé en chapitres, présentés plus haut. 
Chaque chapitre est continue sur une branche git. Pour changer de chapitre, il suffit de changer de branche. 

Les branches sont nommées de la façon suivante : `NUMERO_DE_CHAPITRE.SECTION-DESCRIPTION`. Par exemple : `1.2-les-verbes-http`

    git branch --list 
    git switch MA_BRANCHE