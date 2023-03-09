class KeyEncryption:
    """
    Classe permettant de chiffrer et déchiffrer une chaîne de caractères en utilisant une clé de chiffrement.
    """

    def __init__(self):
        """
        Constructeur de la classe. Initialise les attributs m_key_clean et m_key_encrypted à une chaîne de caractères vide.
        """
        self.m_key_clean = ""
        self.m_key_encrypted = ""

    def setKeyClean(self, key_clean: str):
        """
        Méthode permettant de définir la valeur de l'attribut m_key_clean.

        :param key_clean: La chaîne de caractères à utiliser comme clé de chiffrement en clair.
        """
        self.m_key_clean = key_clean
    
    def setKeyEncrypted(self, key_encrypted: str):
        """
        Méthode permettant de définir la valeur de l'attribut m_key_encrypted.

        :param key_encrypted: La chaîne de caractères à utiliser comme clé de chiffrement chiffrée.
        """
        self.m_key_encrypted = key_encrypted

    def getValueKey(self, key: str):
        """
        Méthode calculant la valeur de la clé de chiffrement.

        :param key: La chaîne de caractères à utiliser comme clé de chiffrement.
        :return: La valeur de la clé de chiffrement.
        """
        value = 0
        for character in key:
            value += ord(character)
        return value

    def getKeyClean(self, key: str = ''):
        """
        Méthode déchiffrant la chaîne de caractères stockée dans l'attribut m_key_encrypted.

        :param key: La clé de chiffrement à utiliser. Si aucune clé n'est spécifiée, la méthode utilise la clé stockée dans l'attribut m_key_clean.
        :return: La chaîne de caractères déchiffrée.
        """
        self.m_key_clean = ""
        for character in self.m_key_encrypted:
            self.m_key_clean += chr(ord(character) - 1) # La valeur de la clé de chiffrement est fixée à 1 dans ce code.
        return self.m_key_clean
    
    def getKeyEncrypted(self, key: str = ''):
        """
        Méthode chiffrant la chaîne de caractères stockée dans l'attribut m_key_clean.

        :param key: La clé de chiffrement à utiliser. Si aucune clé n'est spécifiée, la méthode utilise la clé stockée dans l'attribut m_key_encrypted.
        :return: La chaîne de caractères chiffrée.
        """
        self.m_key_encrypted = ""
        for character in self.m_key_clean:
            self.m_key_encrypted = self.m_key_encrypted + chr(ord(character) + 1) # La valeur de la clé de chiffrement est fixée à 1 dans ce code.
        return self.m_key_encrypted