import urllib.request

# url = "http://uta.pw/shodou/img/28/214.png"
# savename = "data/test.png"
# #urllib.request.urlretrieve(url,savename)

# # download
# mem = urllib.request.urlopen(url).read()

# with open(savename, mode='wb') as f:
#     f.write(mem)
#     print("저장 되었습니다.")

# url = "http://google.co.kr/"

# mem = urllib.request.urlopen(url).read()
# print(mem.decode("euc-kr"))


url = "http://api.aoikujira.com/ip/ini"

mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))
