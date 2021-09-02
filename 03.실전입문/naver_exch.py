from bs4 import BeautifulSoup
import urllib.request as req

# html 가져오기
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

# html 분석
soup = BeautifulSoup(res, "html.parser")

# 원하는 값 추출
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)