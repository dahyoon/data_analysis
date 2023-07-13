# # 해시함수 - 원리 구조 - 면접 시 물어볼 수도 있음!!

# list, tuple, dictionary 간 간단 차이점 
    # 리스트는 a = [value, ...] ; a[index]
    # 튜플은 a = (value, ...) ; a[index]
    # 딕셔너리는 a = {key:value, ...} ; a[key]

# key + value(값)로 이루어짐, {} 사용
# python에서의 dictionary는 다른 language의 map 또는 hashmap과 유사한 자료형, json이라는 자료형태와도 유사
# 영어사전에서 단어와 뜻으로 이루어져있는 것에서 유래
# key는 중복 불가, value는 다른 key에도 존재 가능
    # 예)
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # print(dic1)
        # >> {'이름': '홍길동', '나이': 25, '성별': '남'}
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남', '성별': '여'}
        # print(dic1)
        # >> {'이름': '홍길동', '나이': 25, '성별': '여'} # python에서는 저절로 덮어버린다
# key와 value로 이루어져 있다보니 순서의 의미가 없다: index로 접근 불가
# key로 value 검색 시 해시함수를 통해 index를 찾다보니 매우 빠른 속도 보장

# value 호출 방식
    #dic[key], dic.get(key)
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # print(dic1['나이'])
        # >> 25
        # print(dic1.get('나이'))
        # >> 25

# dic 추가하기
    # dic[key] = value
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # dic1['신분'] = '학생'
        # print(dic1)
        # >> {'이름': '홍길동', '나이': 25, '성별': '남', '신분': '학생'}
    # dic.items() - key value 쌍 얻기; key value 쌍을 튜플로 묶어 dict개체로 변환
        # dict = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # for (x, y) in dict.items():
        #     print(x, y)
        # >>  이름 홍길동
        #     나이 25
        #     성별 남
        # dict = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # print (dict.items())
        # >> dict_items([('이름', '홍길동'), ('나이', 25), ('성별', '남')])

# dic 삭제하기
    # del dic[key]
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # del dic1['성별']
        # print(dic1)
        # >> {'이름': '홍길동', '나이': 25}
    # dic.clear() - 모든 item 제거
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # dic1.clear()
        # print(dic1)
        # >> {}
    # dic.pop() - 지정된 Key가 있는 item remove and return
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # dic1.pop('나이')
        # print(dic1)
        # >> {'이름': '홍길동', '성별': '남'}
# key 목록 출력
    # dic.keys()
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # keyList = dic1.keys()
        # print(keyList)
        # >> dict_keys(['이름', '나이', '성별'])    # type은 <class 'dict_keys'>
    # iterable한 형태로 data가 출려되므로 for문 사용가능 (list는 아님! 그래서 range로 index 출력 불가)
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # keyList = dic1.keys()
        # for a in keyList:
        #     print(a)
        #     >> 이름
        #     >> 나이
        #     >> 성별
# value 목록 출력
    # dic.values()
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # keyList = dic1.values()
        # print(keyList)
        # >> dict_values(['홍길동', 25, '남'])
# key를 출력해주는 for문 안에서 value도 같이 출력
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # keyList = dic1.keys()
        # for k in keyList:
        #     print(k)
        #     print(dic1[k])
        #     >> 이름
        #     >> 홍길동
        #     >> 나이
        #     >> 25
        #     >> 성별
        #     >> 남
# keyList = dic1.keys()와 for k in keyList문을 활용해서 key가 담긴 list를 만들고, value가 담긴 list를 만들어 출력
        # dic1 = {'이름': '홍길동', '나이': 25, '성별': '남'}
        # keyList = dic1.keys()
        # lista = []
        # listb = []
        # for k in keyList:
        #     lista.append(k)
        #     listb.append(dic1[k])
        # print(lista)
        # print(listb)
        # >> ['이름', '나이', '성별']
        # >> ['홍길동', 25, '남']
# dictionary의 확장
    # dic.update(dicnew) - 같은 key의 valye는 덮어버림
        # dic1 = {'a':1, 'b':2, 'c':3}
        # dic2 = {'a':2, 'd':4, 'f':5}
        # dic1.update(dic2)
        # print(dic1)
        # >> {'a': 2, 'b': 2, 'c': 3, 'd': 4, 'f': 5}
# dic 생성
    # dict() - '='사용, key는 문자열 아님('' 안붙임), value는 class에 따라 붙이거나 안 붙임
        # dic1 = dict(이름 = '홍길동', 나이 = 25, 성별 = '남')
        # print(dic1)
        # >> {'이름': '홍길동', '나이': 25, '성별': '남'}

# 연습문제
    # lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB'] 로 dicta = {'A':2, 'B':1, 'O':2, 'AB':2} 출력하기
        # hint: a / not in / dicta.keys() / dic[key] = value
        # 나의 노가다
            # dicta = {}
            # dicta['A'] = lista.count('A')
            # dicta['B'] = lista.count('B')
            # dicta['O'] = lista.count('O')
            # dicta['AB'] = lista.count('AB')
            # print(dicta)
            # >> {'A': 2, 'B': 1, 'O': 2, 'AB': 2}
        # 선생님
            # lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB']
            # dicta = {}
            # for a in lista:
            #     if a not in dicta.keys():
            #         dicta[a] = 1
            #     else:
            #         dicta[a] = dicta[a] + 1
            # print(dicta)
            # >> {'A': 2, 'B': 1, 'O': 2, 'AB': 2}
        # 다른 학생
            # lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB']
            # dicta = {}
            # for a in lista:
            #     if a not in dicta.keys():
            #         dicta[a] = lista.count(a)
            # print(dicta)
            # >> {'A': 2, 'B': 1, 'O': 2, 'AB': 2}
    # 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다. 
    # 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
    # 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
    # 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    # completion의 길이는 participant의 길이보다 1 작습니다.
    # 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    # 참가자 중에는 동명이인이 있을 수 있습니다.
        # 선생님
            # participants = ["mislav", "stanko", "mislav", "ana"]	
            # completion = ["stanko", "ana", "mislav"]	
            # dictc = {}
            # for c in completion:    # completion을 dict로 변환
            #     if c not in dictc.keys():
            #         dictc[c] = 1
            #     else:
            #         dictc[c] = dictc[c] + 1
            # for p in participants:
            #     if p in dictc.keys() and dictc[p] > 0:
            #         dictc[p] = dictc[p] -1
            #     else:
            #         print(p)
            # >> mislav


