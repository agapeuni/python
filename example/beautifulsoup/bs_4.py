import requests
from bs4 import BeautifulSoup

req = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20210708")
html = req.text

soup = BeautifulSoup(html, 'html.parser')
movies_rank = soup.find_all('div', class_="tit5")

for i in range(len(movies_rank)):
    print("{:2} : {}".format(i+1, movies_rank[i].get_text().strip()))
