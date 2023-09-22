# 함수형 프로그램: lambda, map, filter 등 함수를 사용하는 프로그램


# lambda 함수
    # lambda x: 실행문
    # 사용이유: 함수 간단화하기 위해 함수를 변수에 담기 위한 방식

# 기본 구조
    # 함수명 = lambda 매개변수 : 실행문
# 예)
    # add_lambda = lambda a, b : a + b
    # print(add_lambda(1, 2))

# 연습
    # 매개변수 a를 입력했을 때 a의 제곱이 출력되는 lambda 함수 생성
        # myFunc = lambda a: a**2
        # print(myFunc(4))
        # >> 16

# list에 lambda 함수 담아서 사용 가능 (호출방법) 
        # add = lambda a, b : a + b
        # minus = lambda a, b : a - b
        # multiply = lambda a, b : a * b
        # cal_list = [add, minus, multiply]
        # a = cal_list[2](2, 2)
        # print(a)
        # >> 4

        # cal_list = [lambda a, b : a + b, lambda a, b : a - b, lambda a, b : a * b]
        # a = cal_list[2](2, 4)
        # print(a)
        # >> 8

# dictionaty에 lambda 함수 담아서 사용 가능 (호출방법 동일)
        # cal_dict = {'plus': lambda a, b : a + b,
        #             'minus': lambda a, b : a - b,
        #             'multiply': lambda a, b : a * b}
        # print(cal_dict['plus'](1, 2))
        # >> 3
# 삼항 연산자(조건부표현식) 사용하여 lambda로 입력한 매개변수가 짝수이면 Truem 홀수이면 False
        # oddOrNot = lambda x : True if x % 2 == 0 else False





# map 함수
    # 특정 함수와 반복가능한 자료형을 입력받아 특정 함수가 수행한 결과값을 return

# 기본 구조
    # map(함수, 리스트(또는 튜플 등등))
# 예)
    # def two_times(x):
    #     return x * 2
    # lst = list(map(two_times, [1,2,3,4]))
    # print(lst)
    # >> [1, 4, 6, 8]

# map과 lambda 함수를 사용하여 입력한 list의 제곱값을 담은 
    # list 출력
        # lst = list(map(lambda x:x**2, [1, 2, 3]))
        # print(lst)
        # >> [1, 4, 9]
    # set 출력
        # s1 = set(map(lambda x:x**2, [1, 4, 1, 2, 3, 3, 9]))
        # print(s1)
        # >> {1, 4, 9, 16, 81}
    # tuple 출력
        # tup = set(map(lambda x:x**2, [1, 2, 3]))
        # print(tup)
        # >> (1, 4, 9)





# filter 함수

# 기본 구조
    # filter(함수, 리스트(또는 튜플 등등))

# map vs. filter
    # map 역할: 대상이 되는 리스트를 가지고 함수를 적용하여 새로운 리스트를 만드는 것
    # filter 역할: 대상이 되는 리스트에서 함수를 적용하여 참/거짓 조건으로 값을 걸러내는 것
        # def trueOrNot(x):
        #     if x > 0:
        #         return True
        #     else:
        #         return False
        # lst = list(filter(trueOrNot, [-1, 0, 3, -2, 5]))
        # print(lst)    
        # >> [3, 5]
    # 위 로직을 lambda를 써서 바꿔보자(삼항 연산자)
        # filter 사용 (걸러내기)
            # lst = list(filter(lambda x: True if x > 0 else False, [-1, 0, 3, -2, 5]))
            # print(lst)
            # >> [3, 5]
        # map 사용 (적용, 새로운 리스트 출력)
            # lst = list(map(lambda x: True if x > 0 else False, [-1, 0, 3, -2, 5]))
            # print(lst)
            # >> [False, False, True, False, True]


# 함수형 프로그램밍을 사용하여 주어진 list에서 홀수만 추출하도록 하여라
        # lista = [4, 7, 1, 2, 5, 6, 8]
        # lst = list(filter(lambda x: True if x%2 != 0 else False, lista))
        # print(lst)
        # >> [7, 1, 5]





# 재귀 함수
    # 함수 내에서 함수 자기 자신을 호출하는 함수, 반드시 재귀함수를 종료시키는 조건이 들어가야 한다
    # 반복의 횟수를 알 수 없을 떄 재귀함수를 사용
    # 변수 n 을 넣었을 때 n!가 나오도록 함수를 만들어보자
        # 재귀함수 사용 전
            # def factorial(n):
            #     result = 1
            #     for a in range(1, n+1):
            #         result *= a
            #     return result
            # print(factorial(4))
            # >> 24
        # 재귀함수
            # def factorial(n):
            #     if n == 1:
            #         return 1
            #     return n * factorial(n-1)
            # print(factorial(4))
            # >> 24

# 연습
    # 숫자 조합 - 매개변수 list와 조합해야 할 n개의 숫자가 주어질 때 list의 n개씩 조합을 구하여 리스트에 담아 출력
        # def recur(lista, total_list, temp_list, n, m):
        #     if m == 0:
        #         total_list.append(temp_list[:])             # append할 때 그냥 (temp_list)만 하면 주소만 복사하나 값을 복사하고 싶으면 temp_list[:]하면 됨! (시작부터 끝까지라는 뜻)
        #         return
        #     for a in range(n, len(lista)):
        #         temp_list.append(lista[a])
        #         recur(lista, total_list, temp_list, a +1, m-1)
        #         temp_list.pop()

        # lista = [10, 20, 30, 40, 50]
        # total_list = []
        # input2 = 2
        # recur(lista, total_list, [], 0, input2)
        # print(total_list)
    # 숫자 순열 - 개인적으로 시간 날 때 해보기




# 주어진 자료들의 총합
    # sum()
        # 예)
        #     print(sum([1,2,3]))
        #     >> 6
# sum, max, min도 함수형 프로그래밍에 적용 가능
        # lista = [4, 7, 1, 2, 5, 6, 8]
        # sum_value = sum(filter(lambda x: True if x%2 != 0 else False, lista))
        # print(sum_value)

# 문자를 아스키코드 변환
    # ord()
        # print(ord('a'))
        # print(ord('b'))
        # >> 97
        #    98
    # chr()
        # print(chr(97))
        # print(chr(98))
        # >> a
        #    b

    # 예를 들어 문자열이 주어질 때 숫자를 제외하고 문자값만 새로운 문자열로 만들어보아라
        # 소문자 a-z: 97-122
        # 대문자 A-Z: 65-90
            # str1 = '123sdEgfsdAA4fgd323'
            # new_str = ""
            # for a in str1:
            #     if (122>= ord(a) >= 97) or (65<= ord(a) <= 90):
            #         new_str += a
            # print(new_str)
            # >> sdEgfsdAAfgd

# 절대값 구하기
    # abs()
        # print(abs(-3))
        # >> 3

    # map을 사용해서 주어진 리스트를 절대값으로 변환한 리스트 출력
        # lista = [1, -5, 12, -5]
        # print(list(map(abs, lista)))
        # >>[1, 5, 12, 5]