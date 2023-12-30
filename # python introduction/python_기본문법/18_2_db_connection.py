# 실습!
    # 일단,
        # practice 스키마 생성
        # coin_price 테이블 생성 
        # id(pk, auto),
        # coin_name varchar(20),
        # last_price varachar(100), 
        # created_date(datetime, default current_timestamp)
    # python code로 아래 생성
        # 10초마다 "BTCUSDT" 비트코인의 시세를 coin_price에 입력


import requests
import mysql.connector
import json
import time

try:
    connector = mysql.connector.connect(
        host = "localhost", 
        port = "3406", 
        user = "root", 
        password = "1234", 
        database = "practice", 
        use_pure = True)     # 이 부분을 추가
    cursor = connector.cursor()
except mysql.connector.Error as err:
    print(err)
    

# 코인시세 10초에 한번씩 db insert
try:
    while True:
        url = "https://api.binance.com/api/v3/ticker/24hr"
        response = requests.get(url)
        data_json = json.loads(response.text)
        for a in data_json:
            if a['symbol'] == "BTCUSDT":
                add_data = "INSERT INTO coin_price (coin_name, last_price) VALUES (%s, %s)"
                data = (f"{a['symbol']}", f"{a['lastPrice']}")
        cursor.execute(add_data, data)
        connector.commit()
        time.sleep(10)
except mysql.connector.Error as err:
    print(err)

cursor.close()
connector.close()


# 자동입력 멈추고 싶으면 시스템 종료하면 됨 -> ^C를 terminal에 입력 후 enter







    