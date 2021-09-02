from typing import Text
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#매개변수를 URF 인코딩
values = {
    "stnId" : "108"
}

params = urllib.parse.urlencode(values)
#욫ㅇ 전용 url을 생성 한다.
url = API + "?" + params
print("url = ", url)
#다운로드 
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)