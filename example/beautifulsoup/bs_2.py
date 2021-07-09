
from bs4 import BeautifulSoup

html = """
<html>
<head>
</head>
<body>
    <h1 id="title">BeautifulSoup 예제</h1>
    <p>paragraph 1</p>
    <p>paragraph 3</p>
    <p id="paragraph">paragraph 2</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
paragraph = soup.find(id="paragraph")

print()
print("title = ", title)
print("paragraph = ", paragraph)

print()
print("title.string = " + title.string)
print("paragraph.string = " + title.string)

