from bs4 import BeautifulSoup

with open("Python/course.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    #soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

    print(soup)