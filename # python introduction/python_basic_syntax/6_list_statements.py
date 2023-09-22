# list는 변수마다 값을 할당해서 사용하기에 관리의 어려움이 있으므로 한 변수에 값을 집합시켜 놓은 것
# list는 순서가 있고 값의 추가, 삭제, 수정이 가능한 구조를 가지고 있다
# 반면 문자열(예) "hello")은 메모리 내부적으로 list와 유사한 자료구조이나 문자열은 값을 추가하거나 수정할 수가 없다
# list의 경우에 [](대괄호)를 사용하여 데이터를 집합, 내부적으로는 ,(반점)로 구분
# 예)
    # a = "김돌쇠"
    # b = "김갑돌"
    # c = "김갑순"
    # 위 원소들을 한 list에 담아 놓은 것: 하나의 변수로 여러개의 데이터를 관리/집합
    # list = ["김돌쇠", "김갑돌", "김갑순"]
# list 안에는 빈값, 숫자, 문자, 다른 list등이 공존할 수 있다
    # 예) lista = []
    # 예) listb = ['a', 'b', 1, 2, ['hello', 'nice', 'bye']]

# list 안의 각각 값에 접근할 때 index 사용
# lista = ["a", "b", "c", "d", "e", "f"]
#   print(lista[0])
#   print(lista[1])
#   print(lista[2])
#   print(lista[3])
#   print(lista[4])
#   print(lista[5])
# 연습
    # 5번째까지 출력
    #   print(lista[:5])
    #   >> ['a', 'b', 'c', 'd', 'e']
    # 5번째까지 출력한 결과물의 type 출력
    #   print(type(lista[:5]))
    #   >> <class 'list'>

# list의 값을 조회
    # list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
    # 1) 변수 number에 [1,2,3]을 담아 출력
        # list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
        # number = list_ex1[-1]
        # print(number)
        # >>> [1, 2, 3]
    # 2) number에 담은 값중 1과 3을 더해 4를 출력
        # print(number[0]+number[2])
        # >>> 4

# slicing
    # 여러개의 데이터를 범위를 지정해서 가져오고 싶을 때 사용
    # slicing의 결과값은 같은 list로 출력

# list 더하기
    # lista = [1, 2, 3, 4, 5]
    # listb = ['a', 'b', 'c']
    # listc = lista + listb
    # print(listc)
    # >>> [1, 2, 3, 4, 5, 'a', 'b', 'c']

# list 길이 구하기: len()
    # lista = [1, 2, 3, 4, 5]
    # print(len(lista))
    # >> 5

# list 값 수정
    # 1개의 값만 바꿀 땐 1개의 값으로 대체
        # lista = [1, 2, 3, 4, 5]
        # lista[1] = 4
        # print(lista)
        # >> [1, 4, 3, 4, 5]
    # 여러 값을 바꿀 땐 다른 list로 대체
        # lista = [1, 2, 3, 4, 5]
        # lista[2] = [5, 5, 5]
        # print(lista)
        # >> [1, 2, [5, 5, 5], 4, 5]
# list 요소 개수 세기: count()
    # list.count(값)
        # 리스트 중 "1"이 몇 개 있는지 세보시오
        # lista = ["1", "2", "3", "4", "1", "1", "3"]
        # print(lista.count("1"))
        # >> 3
# list 값 삭제하기
    # del 리스트명[인덱스] OR del 리스트명[시작:끝]
        # 리스트 a = [1, 3, 5, 7, 9, 10] 에서 3번째 값을 삭제하라
            # a = [1, 3, 5, 7, 9, 10]
            # del a[2]
            # print(a)
            # >> [1, 3, 7, 9, 10]
        # 리스트 a = [1, 3, 5, 7, 9, 10] 에서 2-5번째 값을 삭제하라
            # a = [1, 3, 5, 7, 9, 10]
            # del a[1:5]
            # print(a)
            # >> [1, 10]

    # list.remove(값)
        # 리스트 a = [1, 3, 5, 7, 9, 10] 에서 2번째 값 (3)을 삭제하라
            # a = [1, 3, 5, 7, 9, 10]
            # a.remove(3)
            # print(a)
            # >> [1, 5, 7, 9, 10]
    # 연습문제
        # 특정한 9라는 값을 모두 제거하기
            # 방법 1
                # lista = [1, 3, 9, 3, 5, 6, 9, 9]
                # count = 0
                # for a in range(0, len(lista)):
                #     if lista[a-count] == 9:
                #           del lista[a-count]
                #           count = count + 1
                # print(lista)
            # 방법 2
                # lista = [1, 3, 9, 3, 5, 6, 9, 9]
                # listb = []
                # for a in range(0, len(lista)):
                #     if lista[a] !=9:
                #           listb = listb + [lista[a]]
                #           또는 listb.append(lista[a])
                # print(listb)
            # 방법 3
                # lista = [1, 3, 9, 3, 5, 6, 9, 9]
                # for a in range(0, len(lista)):
                #     if 9 in lista:
                #           lista.remove(9)
                #     else:
                #           break
                # print(lista)
# list 추가
    # list.append() - 맨 뒤로 추가
        # lista = [1, 3, 5, 7]
        # 9를 append를 이용하여 추가해서 출력
        # lista.append(9)
        # print(lista)
        # >> [1, 3, 5, 7, 9]
        # list를 추가할 수 있음
            # listb = [1, 2, 3]
            # listc = ['a', 'b', 10]
            # listb.append(listc)
            # print(lista)
            # >> [1, 2, 3, ['a', 'b', 10]]
    # list.insert(index, value) - 위치를 지정하여 추가
        # vowel = ['a', 'e', 'i', 'u']
        # 'o'를 index 3 (4번째 자리에 추가하기)
        # vowel.insert(3, 'o')
        # print(vowel)
        # >> ['a', 'e', 'i', 'o', 'u']
    # list.extend() - iterable 객체를 list에 추가할 때 사용 - 각 요소를 꺼내어 맨 뒤에 추가
        # lista = [1, 2, 3]
        # listb = [10, 20, 30]
        # lista.extend(listb)
        # print(lista)
        # >> [1, 2, 3, 10, 20, 30]

# list 정렬
    # lst명.sort() - 오름차순 정렬 - 숫자, 영어, 한국어 다 됨 -> 수정
        # numa = [1, 10, 2, 5, 7, 4]
        # numa.sort()
        # print(numa)
        # >> [1, 2, 4, 5, 7, 10]
        # chlist = ['brad', 'john', 'anna']
        # chlist.sort()
        # print(chlist)
    # lst명.sort(reverse = True) - 내림차순 정렬
    # list.sort(list명) 도 있음!
# list 뒤집기
    # list.reverse()
        # chlist = ['brad', 'john', 'anna']
        # chlist.reverse()
        # print(chlist)
        # >> ['anna', 'john', 'brad']
# list 위치반환
    # list.index(값)
        # lista = ['안','녕','히','가']
        # lista.index('가')
        # print(lista.index('가'))
        # >> 3
# list 마지막 요소 끄집어내기
    # list.pop(값) - remove and return last value
        # lista = [1, 2, 3, 4, 5, 6, 7]
        # lastValue = lista.pop()
        # print(lastValue)
        # >> 7
        # print(lista)
        # >> [1, 2, 3, 4, 5, 6]

# list <-> 문자열 만들기
    # 문자 list를 문자열로 만들기
        # str.join(list)
            # lista = ["hello", "world", "python"]
            # st1 = " "
            # st2 = st1.join(lista)
            # print(st2)
            # >> hello world python
    # 문자열을 문자 list로 만들기
        # list()
            # sta1 = "hello world python"
            # print(list(sta1))
            # >> ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'p', 'y', 't', 'h', 'o', 'n']
        # str.split()
            # sta1 = "hello world python" 
            # print(sta1.split())
            # >> ['hello', 'world', 'python']

# 최대값/최소값 구하기
    # 최대값
        # for문으로 구하기
            # lista = [100, 20, 30, 5, 90]
            # maxA = lista[0]
            # for a in lista:
            #     if maxA < a:
            #         maxA = a
            # print(maxA)
            # >> 100
        # max(list)
            # lista = [100, 20, 30, 5, 90]
            # maxA = max(lista)
            # print(maxA)
            # >> 100
        # list.sort()로 구하기
            # lista = [100, 20, 30, 5, 90]
            # lista.sort()
            # print(lista[-1])
            # >> 100
    # 최소값
        # for문으로 구하기
            # lista = [100, 20, 30, 5, 90]
            # minA = lista[0]
            # for a in lista:
            #     if minA > a:
            #         minA = a
            # print(minA)
            # >> 5
        # min(list)
            # lista = [100, 20, 30, 5, 90]
            # minA = min(lista)
            # print(minA)
            # >> 5
        # list.sort()로 구하기
            # lista = [100, 20, 30, 5, 90]
            # lista.sort()
            # print(lista[0])
            # >> 5

# list 만들기
    # list comprehension - 장점: 간결하다
        # lista = [변수 for 변수 in range(숫자)]
            # 예)
                # lista = [a*2 for a in range(10)]
                # print(lista)
                # >>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    # (lista에 0-9까지 담는 방법)
        # 방법 1 - 노가다
            # lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 방법 2 - list()
            # lista = list(range(10))
            # print(lista)
            # >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 방법 3 - list.append()
            # lista = []
            # for a in range(10):
            #     lista.append(a)
            # print(lista)
            # >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 방법 4 - list comprehension
            # lista = [a for a in range(10)]
            # print(lista)
            # >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # range(0, 10)에서 홀수값만 2배 한 값만을 담은 리스트를 출력
        # for문
            # lista = []
            # for a in range(10):
            #     if a%2 != 0:
            #         lista.append(a*2)
            # print(lista)
            # >> [2, 6, 10, 14, 18]
        # list comprehension 사용하기
            # lista = [a*2 for a in range(10) if a % 2 != 0]
            # print(lista)
            # >> [2, 6, 10, 14, 18]
        # index
            # lista = list(range(10))
            # listb = lista[1:11:2]
            # listc = []
            # for a in listb:
            #     listc.append(a*2)
            # print(listc)
            # >> [2, 6, 10, 14, 18]