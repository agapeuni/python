from bs4 import BeautifulSoup

html = """
<html>
<body>
    <h1>잠언 말씀</h1>
    <p>너는 범사에 그를 인정하라 그리하면 네 길을 지도하시리라 (잠언 3:6)</p>
    <p>사람이 마음으로 자기의 길을 계획할지라도 그걸음을 인도하시는 이는 여호와시니라 (잠언 16:9)</p>
</body>
</html>
"""

# BeautifulSoup 인스턴스를 생성할 때 'html.parser'를 지정한다.
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print()
print("h1 = ", h1)
print("p1 = ", p1)
print("p2 = ", p2)

print()
print("h1.string = " + h1.string)
print("p.string = " + p1.string)
print("p.string = " + p2.string)
