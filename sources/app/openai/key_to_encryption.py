from keyencryption import KeyEncryption

key_api = KeyEncryption()

# Demande à l'utilisateur de saisir une clé et la stocke
# après l'avoir nettoyée à l'aide de la méthode setKeyClean.
key_api.setKeyClean(input('key: '))

# Affiche la version chiffrée de la clé stockée en utilisant
# la méthode getKeyEncrypted de l'objet key_api.
print(key_api.getKeyEncrypted())