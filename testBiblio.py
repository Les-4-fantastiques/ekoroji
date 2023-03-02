from trad import *

siteweb = TradHtml(["index.html", "styleindex.css", "messcans.html", "explorer.html", "stylemesscans.css", "styleindex.css"], "Test_projet1", "testtemplates/")
siteweb.read()
siteweb.tradFiles()