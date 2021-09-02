import urllib.request
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#type06_headline lede")      # 17년과는 다른 html을 가지고있다!!
for result in results:
    print(result.string)