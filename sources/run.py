"""
Ce script est utilisé pour lancer une instance de l'application Flask. Il importe la fonction create_app() depuis le module app pour créer l'application Flask. Il vérifie ensuite que le script est exécuté en tant que programme principal avant de lancer le serveur Flask.

Modules utilisés:
- app: contient la fonction create_app() pour créer l'application Flask

Variables globales:
- app: instance de l'application Flask créée à l'aide de la fonction create_app()

Instructions d'utilisation:
- Exécuter le script à partir de la ligne de commande pour lancer l'application Flask
"""

from app import create_app

# Crée une instance de l'application Flask
app = create_app()

# Vérifie que le script est exécuté en tant que programme principal
if __name__ == '__main__':
    # Lance le serveur Flask
    app.run()
