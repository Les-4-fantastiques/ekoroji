# Importation de la fonction create_app() depuis le module app
from app import create_app

# Création d'une instance d'application Flask
app = create_app()

# Vérification que le script est bien exécuté en tant que programme principal
if __name__ == '__main__':
    # Lancement du serveur Flask
    app.run()
