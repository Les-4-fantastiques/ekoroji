from bs4 import BeautifulSoup
"""
TradHtml(nameFile, nameProject, nameFolder) : qui converti un site web HTML et CSS en un programme python utilisant Flask
"""
class TradHtml:
    def __init__(self, nameFile:list, nameProject:str, nameFolder:str = ""):
        """
        Translate HTML and CSS to python with FLask
        ===========================================
        Parameters
        ----------
        - nameFile : liste des fichiers HTML et CSS du site web à convertir
            - Exemple :
                - "helloWorld.html"
                - "styleHelloWorld.css"
            - IMPORTANT
                - Pour les pages CSS, il est obligatoire de réaliser un fichier CSS par HTML, et non un seul fichier CSS utilisé dans plusieurs fichiers HTML
                - Renommer correctement le fichier CSS en fonction de la page HTML :
                    "hello.html" -> "hello.css" ou "stylehello.css"
                - Une autre orthographe ne sera pas fonctionnelle

        - nameProject : texte indiquant le nom du site final, ce dernier sera le nom du fichier .py avec flask intégré
            - Exemple :
                - "helloWorldProjet"
            - IMPORTANT
                - Ne pas nommer le projet flask sinon le projet sera "flask.py" et le programme ne se lancera pas

        - nameFoler : texte indiquant l'emplacement des fichiers HTML et CSS
            - Exemple :
                - "Project/Flask/helloworld.py" -> "Project/Flask/"
            - IMPORTANT
                - Ne rien mettre si le dossier est le même que celui appelant cette bibliothèque
                - La création des fichiers textes et Project.py se fera dans ce meme repertoire

        Methods
        -------
        - read() : Permet de mettre à jour les fichiers HTML et CSS dans la classe
            - IMPORTANT
                - la méthode n'est pas obligatoire mais sans elle le classe n'aura pas conscience du nouveau contenu des fichiers du site web, ainsi l'emploi est fortement conseillé
                    - Exemple : j'appelle read(), je modifie index.html, le class TradHtml, ne le saura pas il faut rappeler read()
        - tradFiles() : Permet de lancer la conversion des fichiers HTML et CSS en langage python, cette méthode est obligatoire s'il l'on souhaite convertir une site web en programme python
            - IMPORTANT
                - la méthode n'utilisera que la dernière version dont elle a acces grace à la méthode read(), regarder la docstring plus haut

        Returns
        -------
        - retourne des fichiers textes du noms des fichiers HTML, avec comme contenu le programme HTML et CSS et la page actuelle
            - Exemple : "index.txt" -> "index.html" + "styleindex.css"
        - retourne un fichier "Project.py" qui suffit d'executer pour voir le site se créé via python et flask
        - retourne un message de succès de la conversion de chaque fichier dans la console

        IMPORTANT

        - Pour executer le programme flask en suivant, il est necessaire d'installer la biliotheque flask "pip install flask"
        """

        """
        Documentation
        a = TradHtml(['index.html', 'course.html'], 'Python/')
        a.read()
        a.tradFiles()
        """

        self.m_nameProject = nameProject
        self.m_nameFile = nameFile
        self.m_nameFolder = nameFolder
        self.m_directoryFile = []
        for elem in self.m_nameFile:
            self.m_directoryFile.append(self.m_nameFolder + elem)

   
    def read(self):
        """
        read()
        ======
            Permet de mettre à jour les fichiers HTML et CSS dans la classe
            - IMPORTANT
                - la méthode n'est pas obligatoire mais sans elle le classe n'aura pas conscience du nouveau contenu des fichiers du site web, ainsi l'emploi est fortement conseillé
                    - Exemple : j'appelle read(), je modifie index.html, le class TradHtml, ne le saura pas il faut rappeler read()
        """
        self.m_html = []
        self.m_css = []
        for elem in self.m_directoryFile:
            if elem[-5:] == '.html':
                with open(elem, "r") as file_ref:
                    self.m_html.append(elem)
            elif elem[-4:] == '.css':
                self.m_css.append(elem)
        print(self.m_css)

    def tradFiles(self):
        """
        tradFiles()
        ===========
            Permet de lancer la conversion des fichiers HTML et CSS en langage python, cette méthode est obligatoire s'il l'on souhaite convertir une site web en programme python
            - IMPORTANT
                - la méthode n'utilisera que la dernière version dont elle a acces grace à la méthode read(), regarder la docstring plus haut
        """
        with open(f'{self.m_nameFolder}{self.m_nameProject}.py', 'w') as new_file:
            new_file.write(f'from flask import Flask\n\napp = Flask(__name__)\n')
            for elem in self.m_html:
                nameFile = elem.split('/')[-1].split('.')[0]
                new_file.write(f'\n\n"""     {nameFile}     """\n\n')
                self.__tradPageHtml(new_file, elem)
            for elem in self.m_css:
                self.__tradCss(elem)
            new_file.write(f'\n\nif __name__=="__main__":\n    app.run()')

    def __tradPageHtml(self, new_file, fileHtml):
        nameFile = fileHtml.split('/')[-1].split('.')[0]
        directoryFileWithoutExt = fileHtml.split(".")[0]
        if nameFile == 'index':
            new_file.write(f'@app.route("/")\n')
        else:
            new_file.write(f'@app.route("/{nameFile}")\n')
        new_file.write(f'def {nameFile}():\n')
        
        with open(f'{directoryFileWithoutExt}.txt', 'w') as fileText:
            with open(fileHtml, 'r') as fileHtml:
                textHtml = fileHtml.readlines()
                for ligne in textHtml:
                    if 'href' in ligne:
                        ligne = self.__deleteText(ligne, '.html')
                        ligne = self.__deleteText(ligne, 'index', '/')
                        if '.css' in ligne:
                            pass
                    fileText.write(str(ligne))
        new_file.write(f'    with open("{directoryFileWithoutExt}.txt", "r") as file:\n        return file.read().encode("utf-8")')
        print(f'Traduction de {fileHtml} réalisé avec succès !')

    def __tradCss(self, directory_fileCss):
        name_file = self.__deleteText(directory_fileCss, 'style')
        directoryFileWithoutExt = name_file.split(".")[0]
        with open(f'{directoryFileWithoutExt}.txt', 'a') as fileHtml:
            with open(directory_fileCss, 'r') as fileCss:
                fileHtml.write(f'\n\n<style>"\n{fileCss.read()}\n"</style>')
        print(f'Traduction de {directory_fileCss} réalisé avec succès !')

    def __deleteText(self, text, deleteMessage, ReplaceMessage = ''):
        if deleteMessage in text:
            for i in range(len(text)-len(deleteMessage)):
                if text[i:i+len(deleteMessage)] == deleteMessage:
                    text = f'{text[:i]}{ReplaceMessage}{text[i+len(deleteMessage):]}'
        return text