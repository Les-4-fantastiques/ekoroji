<div class="banner", align="center">
  <img src="sources/app/static/assets/logos/Ekoroji_light.svg" alt="Logo de Ekoroji" width="150" height="150" align="center">
</div>

---

<div align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/Les-4-fantastiques/Ekoroji?style=for-the-badge">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Les-4-fantastiques/Ekoroji?style=for-the-badge">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Les-4-fantastiques/Ekoroji?style=for-the-badge">
</div>
<br>
<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/-Python-FFD43B?logo=python&logoColor=306998&style=for-the-badge">
  <img alt="Flask" src="https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=FFFFFF&style=for-the-badge">
  <img alt="SQLAlchemy" src="https://img.shields.io/badge/-SQLALCHEMY-cd2103?logo=sqlite&logoColor=ebebeb&style=for-the-badge">
  <img alt="OpenAI API" src="https://img.shields.io/badge/-OPENAI%20API-1ea47f?logo=openai&logoColor=FFFFFF&style=for-the-badge">
  <img alt="HTML 5" src="https://img.shields.io/badge/-HTML5-F06529?logo=html5&logoColor=FFFFFF&style=for-the-badge">
  <img alt="CSS 3" src="https://img.shields.io/badge/-CSS%203-2965f1?logo=css3&logoColor=FFFFFF&style=for-the-badge">
</div>

---

# Ekoroji

Ekoroji est une application web conçue pour simplifier la recherche et la gestion des déchets. Elle est construite en utilisant le framework Flask et l'API OpenAI pour fournir des informations précises et fiables sur les différents types de déchets. Les utilisateurs peuvent rechercher des déchets spécifiques à l'aide d'un formulaire de recherche convivial et trouver des informations détaillées sur leur gestion, leur recyclage, leur réutilisation et leur élimination.

Ekoroji offre également la possibilité aux utilisateurs de contribuer à la base de données en ajoutant des informations sur les déchets. Ils peuvent ajouter, modifier ou supprimer les déchets existants pour maintenir la base de données à jour et pertinente.

En plus de cela, Ekoroji propose des fonctionnalités de filtrage des résultats de recherche pour permettre aux utilisateurs de trouver des informations spécifiques en fonction de nom, description, etc. L'application fournit également des informations utiles sur les différentes options de gestion des déchets, telles que le tri et le recyclage.

En somme, Ekoroji est une application web pratique et complète pour la recherche et la gestion des déchets. Elle fournit des informations fiables et précises sur les différents types de déchets, tout en permettant aux utilisateurs de contribuer à la base de données et de trouver des informations spécifiques selon leurs besoins. Ekoroji encourage les utilisateurs à adopter une approche responsable dans la gestion de leurs déchets et à contribuer à la protection de l'environnement.

[La vidéo de présentation](https://youtu.be/ZPgcD9z6ZF8)

---

## Technologies utilisées

Ekoroji est construite en utilisant les technologies suivantes :

- Python 3.x
- Flask
- L'API OpenAI

---

## Configuration de la clé d'API OpenAI

Avant de pouvoir exécuter Ekoroji, vous devez configurer votre clé d'API OpenAI. Voici les étapes à suivre :

1. Créez un compte sur la plateforme RapidAPI.
2. Accédez à la page de l'API OpenAI sur RapidAPI.
3. Abonnez-vous à l'API pour obtenir votre clé d'API.
4. Ouvrez le fichier openai/keyencryption.py.
5. Utilisez le code ci-dessous pour configurer votre clé d'API (src/app/openai/key_to_encryption.py):
    ```python
    from keyencryption import KeyEncryption

    key_api = KeyEncryption()
    key_api.setKeyClean(input('key: '))
    print(key_api.getKeyEncrypted())
    ```
6. Copiez la clé d'API chiffrée retournée.
7. Ouvrez le fichier src/app/openai/key_api.txt.
8. Remplacez la valeur déjà présente par la clé d'API chiffrée que vous avez copiée.

Maintenant, vous êtes prêt à exécuter Ekoroji en utilisant votre clé d'API OpenAI configurée.

## Installation et exécution de l'application

1. Cloner le projet Ekoroji depuis GitHub en utilisant la commande suivante :
    ``` bash
    >>> git clone https://github.com/Les-4-fantastiques/ekoroji.git
    ```
2. Naviguez vers le répertoire du projet avec la commande :
    ``` bash
    >>> cd ekoroji
    ```
3. Installez les bibliothèques requises avec la commande suivante :
    ``` bash
    >>> pip install -r requirements.txt
    ```
4. Vous pouvez maintenant exécuter l'application avec la commande suivante :
    ``` bash
    >>> python sources/run.py
    ```
5. Ouvrez votre navigateur et accédez à l'adresse http://localhost:5000 pour voir l'application Ekoroji en action.

Assurez-vous d'avoir Python 3.x installé sur votre système avant de commencer. Si ce n'est pas le cas, téléchargez-le depuis le site officiel de Python et installez-le.

---

## Fonctionnalités de l'application

L'application Ekoroji permet de :

- Recherche d'informations sur les déchets en utilisant l'API OpenAI.
- Ajout, modification et suppression d'articles.
- Affichage de la liste des articles.
- Recherche d'articles à l'aide d'un formulaire de recherche.

---

## Contributeurs

- [@untypequicode](https://github.com/untypequicode) : manager | développeur Python | développeur web
- [@ambre66160](https://github.com/ambre66160) : développeuse web
- [@benoiurlc](#) : responsable de base de données
- [@ghostizzoks](#) : développeur Python

---

## Galerie d'images
<center>
<h4>Les pages principales</h4>
<p float="left">
  <img src="doc/img/Ekoroji_articles.png" width="32%" />
  <img src="doc/img/Ekoroji_index.png" width="32%" /> 
  <img src="doc/img/Ekoroji_popular.png" width="32%" />
</p>
<h4>Les déchets</h4>
<p float="left">
  <img src="doc/img/Ekoroji_waste-new.png" width="24%" />
  <img src="doc/img/Ekoroji_waste.png" width="24%" /> 
  <img src="doc/img/Ekoroji_waste-details.png" width="24%" />
  <img src="doc/img/Ekoroji_waste-delete.png" width="24%" />
</p>
<h4>Les articles</h4>
<p float="left">
  <img src="doc/img/Ekoroji_article-new.png" width="32%" />
  <img src="doc/img/Ekoroji_article.png" width="32%" /> 
  <img src="doc/img/Ekoroji_article-delete.png" width="32%" />
</p>
</center>
