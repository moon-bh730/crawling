from bs4 import BeautifulSoup
fp = open("fruits_veg.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

# css 선택자로 추출
#print(soup.select_one("li:nth-of-type(8)").string)                  #(※1)      ## css 형식이 몇개 안먹히는데 이건 나중에 찾자!! 시간 너무 오래 걸림
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)       #(※2)
#print(soup.select("#ve-list > li[data-lo='us']")[1].string)         #(※3)
print(soup.select("#ve-list > li.black")[1].string)                 #(※4)

# find 메서드로 추출하기
cond = {"data-lo":"us", "class":"black"}
# print(soup.find("li", cond).string)

# find 메서드를 연속적으로 사용하기
# print(soup.find(id="ve-list").find("li",cond).string)

print(soup.select_one("li").head())