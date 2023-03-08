from Translation import *
from Waste import *
"""
a = TradHtml(['index.html', 'informer.html', 'populaire.html', 'styleindex.css', 'styleinformer.css', 'stylepopulaire.css'], "Ekoroji", 'sources/client/')
a.read()
a.tradFiles()

import Ekoroji
Ekoroji.run()
"""

object = Waste('pomme')
print(object.getRecyclingInstructions())
print(object.getDescription())
(object.getPicture()).show()