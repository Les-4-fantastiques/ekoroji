class Config():
    """
    Classe contenant les configurations pour l'application Flask.

    Attributes:
    -----------
    SECRET_KEY : str
        Clé secrète utilisée pour la sécurité de l'application.
    SQLALCHEMY_DATABASE_URI : str
        URI de la base de données.
    UPLOAD_FOLDER : str
        Dossier pour l'enregistrement des fichiers uploadés.
    """
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ekoroji.db'
    UPLOAD_FOLDER = 'app/static/uploads'
