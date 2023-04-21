<p align="center"><img src="src\app\static\assets\logos\Ekoroji_light.svg" align="center" alt="Icon" width="128"/></p>

## <p align="center">Ekoroji</p>

<p align="center">Ekoroji est une application web qui vous permet de rechercher des informations sur les déchets et les articles. Cette application est construite en utilisant Flask et l'API OpenAI.</p>


## <p align="center">Auteur(e)s</p>

- [@untypequicode](https://github.com/untypequicode) manager | python developer
- [@ambre66160](https://github.com/ambre66160) web developer
- @benoiurlc database manager
- @ghostizzoks python developer


## <p align="center">Documentation</p>

Il est nécessaire d'installer la bibliothèque Flask, ainsi au lancement du fichier Ekoroji.py. Ensuite il sera possible d'accéder au site web depuis l'adresse url fourni dans le terminal.

Il est egalement disponible une bibliothèque permettant de convertir un site web entier HTML et CSS en programme python grace au fichier "trad.py".


## <p align="center">Captures d'écran</p>

<p align="center">
<img src="doc/img/Ekoroji_app_informer.png" alt="Ekoroji_app_informer.png" width=30%/>
<img src="doc/img/Ekoroji_app_explorer.png" alt="Ekoroji_app_explorer.png" width=30%/>
<img src="doc/img/Ekoroji_app_scans.png" alt="Ekoroji_app_scans.png" width=30%/>
</p>


## <p align="center">Utilisation / Exemples</p>

Pour utiliser la bibliothèque disponible "trad.py"

```python
from trad import *

siteweb = TradHtml([index.html, index.css, compte.html, compte.css], "Nom_du_site_web", "Emplacement fichiers HTML et CSS")
siteweb.read()
siteweb.tradFiles()

>>>"Nom_du_site_web.py"
```
