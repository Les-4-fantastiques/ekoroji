from Translation import *
from Waste import Waste


a = TradHtml(['index.html', 'informer.html', 'populaire.html', 'styleindex.css', 'styleinformer.css', 'stylepopulaire.css'], "Ekoroji", 'sources/client/')
a.read()
a.tradFiles()

import Ekoroji
Ekoroji.run()


"""
object = Waste('brique de lait')
images = object.getPictures()
i = 0
for image in images:
    image.save(f'{object.getName()}_{i}.png')
    i += 1
print(object.getRecyclingInstructions())
print(object.getDescription())
"""