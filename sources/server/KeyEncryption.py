class KeyEncryption():

    def __init__(self):
        self.m_key_clean = ""
        self.m_key_encrypted = ""

    def setKeyClean(self, key_clean:str):
        self.m_key_clean = key_clean
    
    def setKeyEncrypted(self, key_encrypted:str):
        self.m_key_encrypted = key_encrypted

    def getValueKey(self, key:str):
        value = 0
        for character in key:
            value += ord(character)
        return value

    def getKeyClean(self, key:str):
        #self.m_key_clean = ""
        for character in self.m_key_encrypted:
            self.m_key_clean += chr(ord(character) - self.getValueKey(key))
        return self.m_key_clean
    
    def getKeyEncrypted(self, key:str):
        #self.m_key_encrypted = ""
        for character in self.m_key_clean:
            self.m_key_encrypted = self.m_key_encrypted + chr(ord(character) + self.getValueKey(key))
        return self.m_key_encrypted
    
a = KeyEncryption()
a.setKeyClean("")
b = a.getKeyEncrypted('Ekoroji')
print(b)