import math
# 위는 math라는 라이브러리를 선언하는 것
# pow(a,b) - 2의 10제곱
    # print(math.pow(2,10))
# sqrt(a) - 1024의 제곱근을 구하라
    # print(math.sqrt(1024))





import requests
from bs4 import BeautifulSoup

# 웹으로 주고받는 통신 프로토콜(약속)을 http통신이라 한다
# http 통신을 하기 위해서는 http통신규격에 맞게 request를 서버로 전달해야 한다
# request는 header와 body로 이루어져있다
# 마찬가지로 응답(response)도 header와 body로 이루어져있다

# tag 정보를 갖고 html_response에서 원하는 정보 추출




# 코인시세 10초에 한번씩 db insert
import time
while True:
    print("hello world")
    time.sleep(10)




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





# mysql, 파이썬 연동 라이브러리

# pip install mysql-connector-python을 terminal에다 적어서 깔기
import mysql.connector
connector = mysql.connector(host = "localhost", port = "3306", user = "root", password = "1234", database = "board")

# 커서객체는 데이터베이스에서 쿼리의 결과를 검색하고 순회하는데 사용되는 객체
cursor = connector.cursor()
add_data = "INSSERT INTO author (name, email) VALUES (%s, %s)"
data = ("John", "hello2@naver.com")
cursor.execute(add_data, data)
connector.commit()
cursor.close()
connector.close()