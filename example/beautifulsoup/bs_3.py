from bs4 import BeautifulSoup

html = """
<html>
<body>
<div class='offiece'>
    <p>Word</p>
    <p>Excel</p>
</div>
<div class='language'>
    <p>Python</p>
    <p>Java</p>
    <p>C#</p>
</div>
<ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.google.com">google</a></li>
</ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
lang = soup.find('div', class_='language')
print("lang = ", lang)

print()
links = soup.find_all("a")
for a in links:
    print("a = ", a)

print()
for a in links:
    href = a.attrs['href']
    text = a.string
    print("href = ", href)
    print("text = ", text)
