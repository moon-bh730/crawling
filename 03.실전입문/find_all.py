## id로 요소 찾기
from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

#html 분석!!
soup = BeautifulSoup(html, "html.parser")

# find_all()로 원하는 부분 추출
links = soup.find_all("a")

#찾은것 출력
for a in links:
    href = a.attrs["href"]
    text = a.string
    print(text, ">", href)