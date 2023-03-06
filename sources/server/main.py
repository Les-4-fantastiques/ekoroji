from trad import *

a = TradHtml(['index.html', 'informer.html', 'populaire.html', 'styleindex.css', 'styleinformer.css', 'stylepopulaire.css'], "Ekoroji", 'sources/client/')
a.read()
a.tradFiles()

import Ekoroji
Ekoroji.run()