from keyencryption import KeyEncryption

key_api = KeyEncryption()
key_api.setKeyClean(input('key: '))
print(key_api.getKeyEncrypted())