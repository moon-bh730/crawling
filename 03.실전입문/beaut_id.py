## id로 요소 찾기
from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">스크레이핑이란?</h1>
    <p id="body">웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>    
</body></html>
"""

#html 분석!!
soup = BeautifulSoup(html, "html.parser")

# find()로 원하는 부분 추출
title = soup.find(id="title")
body = soup.find(id="body")

#찾은것 부분 출력
print("#title=" + title.string)
print("#body=" + body.string)