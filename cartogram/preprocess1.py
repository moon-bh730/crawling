import numpy as np
import pandas as pd
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings('ignore')       #경고 무시


BORDER_LINES = [
    [(5, 1), (5,2), (6,2), (6,3), (11,3), (11,0)], # 인천
    [(4,4), (4,5), (2,5), (2,7), (4,7), (4,9), (7,9), 
     (7,8), (8,8), (8,6), (9,6), (9,4), (4,4)], # 서울
    [(1,7), (1,8), (3,8), (3,10), (10,10), (10,7), 
     (12,7), (12,6), (11,6), (11,5), (12, 5), (12,4), 
     (11,4), (11,3)], # 경기도
    [(8,10), (8,11), (6,11), (6,12)], # 강원도
    [(12,5), (13,5), (13,4), (14,4), (14,5), (15,5), 
     (15,4), (16,4), (16,2)], # 충청북도
    [(16,4), (17,4), (17,5), (16,5), (16,6), (19,6), 
     (19,5), (20,5), (20,4), (21,4), (21,3), (19,3), (19,1)], # 전라북도
    [(13,5), (13,6), (16,6)], # 대전시
    [(13,5), (14,5)], #세종시
    [(21,2), (21,3), (22,3), (22,4), (24,4), (24,2), (21,2)], #광주
    [(20,5), (21,5), (21,6), (23,6)], #전라남도
    [(10,8), (12,8), (12,9), (14,9), (14,8), (16,8), (16,6)], #충청북도
    [(14,9), (14,11), (14,12), (13,12), (13,13)], #경상북도
    [(15,8), (17,8), (17,10), (16,10), (16,11), (14,11)], #대구
    [(17,9), (18,9), (18,8), (19,8), (19,9), (20,9), (20,10), (21,10)], #부산
    [(16,11), (16,13)], #울산
    [(27,5), (27,6), (25,6)],
]

#------------------------------------------
# 함수 선언부 -----------------------------
#------------------------------------------
def drawKorea(targetData, blockedMap, cmapname, border_lines=BORDER_LINES):
    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData]))*0.25 + min(blockedMap[targetData])

    datalabel = targetData
    
    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])

    mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    
    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, 
               edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row5 in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 광역시 이름도 같이 표시 
        if len(row5.ID.split())==2:
            dispname = f'{row5.ID.split()[0]}\n{row5.ID.split()[1]}'
        elif row5.ID[:2]=='고성':
            dispname = '고성'
        else:
            dispname = row5.ID

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if row5[targetData] > whitelabelmin else 'black'
        plt.annotate(dispname, (row5['x']+0.5, row5['y']+0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계 표시
    for path in border_lines:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()

# 표현하고자 하는 값에 음수가 있을 경우 처리해주기 위해 약간 수정
def drawKoreaMinus(targetData, blockedMap, cmapname):    
    whitelabelmin = 20.

    datalabel = targetData

    tmp_max = max([ np.abs(min(blockedMap[targetData])), 
                                  np.abs(max(blockedMap[targetData]))])
    vmin, vmax = -tmp_max, tmp_max

    mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    
    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, 
               edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 광역시 이름도 같이 표시 
        if len(row.ID.split())==2:
            dispname = f'{row.ID.split()[0]}\n{row.ID.split()[1]}'
        elif row.ID[:2]=='고성':
            dispname = '고성'
        else:
            dispname = row.ID

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if np.abs(row[targetData]) > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계 그린다.
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()

##------------------------------------------
## 전역변수부  -----------------------------
##------------------------------------------

##------------------------------------------
## 메인 코드부 -----------------------------
##------------------------------------------
df = pd.read_csv('data/시군구_성_연령_5세_별_인구2_2020.csv', encoding='euc-kr')

#print(df.shape)                    #(행, 열) 크기를 출력
#print(df.head(260).tail(5))        #260행에서 tail 5건을 읽어온다, 숫자가 없으면 기본 5건을 가져온다.

df.to_csv('data/1차.csv', encoding="utf-8-sig")         #행정구 컬럼이 대부분 비어있다 & 앞쪽에 블랭크도 들어간 경우도 있음

# df1 = df['시군구'][df.행정구.notnull()]                 #순서번호와 행정구가 널이 아닌것만 가져온다
# df1.to_csv('data/df1.csv', encoding="utf-8-sig")
# df2 = df.행정구[df.행정구.notnull()]
# df2.to_csv('data/df2.csv', encoding="utf-8-sig")

df['시군구'][df.행정구.notnull()] = df.행정구[df.행정구.notnull()]      #행정구가 있는 시군구에 행정구의 값을 대체처리 - 왜지?
# df.to_csv('data/2차.csv', encoding="utf-8-sig")                         #head, tail로 10건 안되는 데이터를 보는건 답답하다.

# 소계 데이터 제외
df = df[df.시군구 != '소계']

# 지방소멸위험지수 = 가임여성인구 / 65세 이상 인구
df['20~39세'] = df['20 - 24세'] + df['25 - 29세'] + df['30 - 34세'] + df['35 - 39세']           # 20~39세 집계작업 = (분모)가임여성 집계위한 사전작업
df['65세이상'] = df['65 - 69세'] + df['70 - 74세'] + df['75 - 79세'] + df['80세 이상']          # 65세 이상 집계작업 = (분자)65세 이상 인구
#df.to_csv('data/3차.csv', encoding="utf-8-sig")
df = df[['광역시도','시군구','구분','인구수','20~39세','65세이상']]                        # 필요한 컬럼만 추출
#df.to_csv('data/4차.csv', encoding="utf-8-sig")

# pivot_table을 만들어서 시군구 단위로 grouping
# 9개의 컬럼으로 나누어짐
# '인구수','20~39세','65세이상'가 (남녀계, 남자 , 여자)로 분기됨
pop = pd.pivot_table(df,index=['광역시도','시군구'], columns=['구분'],
                     values=['인구수','20~39세','65세이상'])
#pop.to_csv('data/5차.csv', encoding="utf-8-sig")

# 인구 소멸비율 계산
pop['소멸비율'] = pop['20~39세','여자'] / pop['65세이상','계']

# 소멸비율 등급별 구분을 조건식으로 True, False 값을 할당
pop['소멸위기지역'] = pop.소멸비율 < 0.5
pop['소멸위기고위험지역'] = pop.소멸비율 < 0.2

# 인구소멸 위기지역, 고위험지역 추출 (불필요한 로직)
# crisis_region = pop[pop.소멸위기지역].index.get_level_values(1)
# high_crisis_region = pop[pop.소멸위기고위험지역].index.get_level_values(1)

# 2중 타이틀을 합쳐서 1줄 col_name로 치환하는 작업
tmp_col = [pop.columns.get_level_values(0)[i] + \
           pop.columns.get_level_values(1)[i]
           for i in range(len(pop.columns.get_level_values(0)))]
pop.columns = tmp_col

pop.reset_index(inplace=True)           # 인덱스 자동 잡도록 지시(제목 치환 후 하는게 맞을듯)
pop['시군구'] = pop.시군구.apply(lambda x: x.strip())   #시군구의 공백 문자열 제거

# index=False로 index col 제거
#pop.to_csv('data/전처리완료.csv', encoding='euc-kr', index=False)

tmp_gu_dict = {
    '수원': ['장안구', '권선구', '팔달구', '영통구'], 
    '성남': ['수정구', '중원구', '분당구'], 
    '안양': ['만안구', '동안구'], 
    '안산': ['상록구', '단원구'], 
    '고양': ['덕양구', '일산동구', '일산서구'], 
    '용인': ['처인구', '기흥구', '수지구'], 
    '청주': ['상당구', '서원구', '흥덕구', '청원구'], 
    '천안': ['동남구', '서북구'], 
    '전주': ['완산구', '덕진구'], 
    '포항': ['남구', '북구'], 
    '창원': ['의창구', '성산구', '진해구', '마산합포구', '마산회원구']
}

metro_list = ['서울특별시','부산광역시','대구광역시','인천광역시','대전광역시','광주광역시','울산광역시']
si_name = [None] * len(pop)

# print(len(pop))
# print(len(pop.시군구.unique()))
# print(len(si_name))

for i in pop.index:
    if pop.광역시도[i] in metro_list:
        if len(pop.시군구[i]) == 2:
            si_name[i] = pop.광역시도[i][:2] + ' ' + pop.시군구[i]
        else:
            si_name[i] = pop.광역시도[i][:2] + ' ' + pop.시군구[i][:-1]     # 긴 구 이름에서 '구' 제외
    else:
        if pop.시군구[i][:-1] == '고성':
            if pop.광역시도[i] == '강원도':
                si_name[i] = '고성(강원)'
            else:
                si_name[i] = '고성(경남)'
        else:
            si_name[i] = pop.시군구[i][:-1]            

        for key, values in tmp_gu_dict.items():
            if pop.시군구[i] in values:
                if len(pop.시군구[i]) == 2:
                    si_name[i] = key + ' ' + pop.시군구[i]
                elif pop.시군구[i] in ['마산합포구', '마산회원구']:
                    si_name[i] = key + ' ' + pop.시군구[i][2:-1]
                else:
                    si_name[i] = key + ' ' + pop.시군구[i][:-1]

# print(len(si_name))
# print(si_name)

pop['ID'] = si_name         # 정리한 지역정보의 컬럼 추가
del pop['20~39세남자']      # 불필요한 컬럼 제거
del pop['65세이상남자']     # 불필요한 컬럼 제거
del pop['65세이상여자']     # 불필요한 컬럼 제거

#pop.to_csv('data/전처리완료.csv', encoding='euc-kr', index=False)

#엑셀 지도모양 가져오기
map_raw = pd.read_excel('data/draw_korea_raw(2021).xlsx')

# stack() : 데이터 재 구조화
map = pd.DataFrame(map_raw.stack())             # 엑셀의 row, col 좌표와 지역값으로 재구성
map.reset_index(inplace=True)
#map.to_csv('data/map01.csv', encoding='euc-kr', index=False)

plt.figure(figsize=(8,11))

for idx, row in map.iterrows():
    # 광역시는 구 이름이 겹치는 경우가 많아서 광역시 이름도 같이 표시 
    # (중구, 서구 등)
    if len(row.ID.split()) == 2:
        dispname = f'{row.ID.split()[0]}\n{row.ID.split()[1]}'
    elif row.ID[:2]=='고성':
        dispname = '고성'
    else:
        dispname = row.ID

    # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시
    if len(dispname.splitlines()[-1]) >= 3:
        fontsize, linespacing = 9.5, 1.5
    else:
        fontsize, linespacing = 11, 1.2

    plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                 fontsize=fontsize, ha='center', va='center', 
                 linespacing=linespacing)
    
# 시도 경계
for path in BORDER_LINES:
    ys, xs = zip(*path)
    plt.plot(xs, ys, c='black', lw=1.5)

plt.gca().invert_yaxis()
#plt.gca().set_aspect(1)

plt.axis('off')

plt.tight_layout()
plt.show()

# pop = pd.merge(pop, map, how='left', on='ID')

# # Null 데이터가 있는지 확인
# print(pop.isnull().sum().sum())
