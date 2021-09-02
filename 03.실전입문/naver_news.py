import urllib.request
from bs4 import BeautifulSoup
import time

# url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# response = urllib.request.urlopen(url)

# soup = BeautifulSoup(response, "html.parser")
#results = soup.select("#type06_headline lede")      # 17년과는 다른 html을 가지고있다!!

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1. 태그 분석 기본속성!!! id는 유니크하고 class는 여러개가 있을 수 있다!
#
# 2. 다음과 같이 클래스가 복잡한 경우 앞의것(nclicks)만 가져다 사용한다.
# <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=105&amp;oid=032&amp;aid=0003095939" 
# class="nclicks(itn.airscont,'8800006B_000000000000000003095939', 'airsGParam', '0', 'news_sec_v2.0', 'Y6aYj8w0tkfQFPRj')">
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# results = soup.select_one(".lnk_hdline_article")
# for result in results:
    # 기사를 가져옵니다.
    # print("제목:", result.attrs["title"])
    # url_article = result.attrs["href"]
    # response = urllib.request.urlopen(url_article)
    # soup_article = BeautifulSoup(response, "html.parser")
    # content = soup_article.select_one("#articleBodyContents")
    # 가공합니다.
    # output = ""
    # for item in content.contents:
    #     stripped = str(item).strip()
    #     if stripped == "": 
    #         continue
    #     if stripped[0] not in ["<", "/"]:
    #         output += str(item).strip()
    # print(output.replace("본문 내용TV플레이어", ""))
    # print()
    # # 30초 휴식
    # time.sleep(1)

header = {'User-agent' : 'Nozila/2.0'}
response = urllib.request.urlopen("https://news.naver.com", headers = header )
html = response.text
soup = BeautifulSoup(html, "html.parser")
title = soup.select_one(".lnk_hdline_article")
print(title)