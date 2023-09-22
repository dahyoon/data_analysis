# while True:
#     # https://로 시작하는 url html 정보 다 가져오기
#     if aaa tag in alist:
#         click
#         while True:
#             실행문

# json: key value로 이루어져 있는 데이터 형식, 아직 정제되어있지 않은 데이터, {}로 감싸져있음
 
# 아래 모듈은 외장 라이브러리이므로, 별도 설치 필요
# 설치 시 pip라는 패키지tool을 이용 (python 설치시 동시에 pip설치된다)
# 설치 방법:
        # 1 terminal에 밑 중 하나 입력 후 enter:
                # python3 --version 
                # pip --version
                # python -m pip --version
        # 2 terminal에 밑 중 하나 입력 후 enter
                # pip install requests
                # python3 -m pip install requests
        # 3 업그레이드 하라고 하면 해줌
                # python3 -m pip install  bs4   
                # python3 -m pip install --upgrade pip

import requests
from bs4 import BeautifulSoup

# 웹으로 주고받는 통신 프로토콜(약속)을 http통신이라 한다
# http 통신을 하기 위해서는 http통신규격에 맞게 request를 서버로 전달해야 한다
# request는 header와 body로 이루어져있다
# 마찬가지로 응답(response)도 header와 body로 이루어져있다

# tag 정보를 갖고 html_response에서 원하는 정보 추출




# 아바타 위키백과에서 감독 정보, 제작비 정보 출력
url = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'
header = {'User-Agent' : 'Mozilla/5.0'}
response = requests.get(url, headers=header)
html_response = BeautifulSoup(response.text, 'html.parser')             # BeautifulSoup 안에 .select_one()이라는 함수 지원
for sup in html_response.find_all('sup'):                               # 제작비 정보를 갖고올 떄 [1]라는 문자열을 지우기 위해 사용됨
        sup.decompose()                                                 # 어떤 것을 없애는 함수 .decompose()

director_info = html_response.select_one('table.infobox > tbody > tr:nth-of-type(3) > td').get_text()    
budget_info = html_response.select_one('table.infobox > tbody > tr:nth-of-type(16) > td').get_text()           
print(f"아바타의 감독은 {director_info}이고 제작비는 {budget_info}이다.")
# >> 아바타의 감독은 제임스 카메론이고 제작비는 2억 5,000만 달러이다.




# 코인 시세 정보 API url
import json
url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)
data_json = json.loads(response.text)

# 출력 결과
# "symbol": "BTCUSDT", "lastPrice": 가격
for a in data_json:
        if a['symbol'] == "BTCUSDT":
                print(f"{a['symbol']}코인의 price는 {a['lastPrice']}이다.")





# csv 파일 parsing
import seaborn
from matplotlib import pyplot
import pandas

file_path = '/Users/dayoonz/Desktop/안다윤/tips.csv'            # 찾고자 하는 디렉토리 주소 선언
csv_data = pandas.read_csv(file_path)
print(csv_data)

# 성별에 따라 tip이 어떻게 달라지는지
# day에 따라 tip이 어떻게 달라지는지
tip_by_gender = csv_data.groupby('gender')['tip'].agg(['mean', 'std']).reset_index()              # .groupby() 함수    # .agg() 집계함수  
                                                                                                  # # .agg():집계함수 ; mean:평균 ; std:표준편차
tip_by_day = csv_data.groupby('day')['tip'].agg(['mean', 'std']).reset_index() 
seaborn.barplot(x='gender', y='mean', data=tip_by_gender, yerr=tip_by_gender['mean'], capsize = 0.1)
seaborn.despine()                                               # .despine() 테두리 없애주는 함수
pyplot.title('average tip per gender')
pyplot.xlabel('gender')
pyplot.ylabel('average tip (%)')
pyplot.show()           # 차트로 나올 것임