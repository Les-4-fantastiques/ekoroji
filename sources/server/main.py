from trad import *

a = TradHtml(['index.html', 'explorer.html', 'messcans.html', 'styleexplorer.css', 'styleindex.css', 'stylemesscans.css'], "Ekoroji", 'sources/client/')
a.read()
a.tradFiles()

import Ekoroji
Ekoroji.run()