# dom, xml, html 요소에 접근하는 구조
from bs4 import BeautifulSoup
soup = BeautifulSoup(
    "<p><a href='a.html'>test</a></p>"
    ,"html.parser"
)

# 분석이 제대로 됬는지 확인
soup.prettify()