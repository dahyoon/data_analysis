# for문의 기본 구조
    # 예)
        # for 변수 in 반복가능한자료형(iterable): #예) list, cell, tuple, string
        #   실행문
    # 예)
        # lista = [10, 20, 30]
        # for a in lista:
        #     print(a)
        #     >> 10
        #     >> 20
        #     >> 30
    # for a in list 구문으로는 원본리스트 데이터 변경 불가
        # 예) 아래와 같은 방식으로는 원본 lista의 값 변경 불가
            # lista = [10, 20, 30, 40]
            # for a in lista:
            #     a = 100 
            # >> [10, 20, 30, 40]
        # 아래와 같은 방식으로 해야 원본리스트 데이터 변경 (list 값 변경)
            # lista = [10, 20, 30, 40]
            # for a in range(len(lista)):
            #     lista[a] = 100
            # print(lista)
            # >> [100, 100, 100, 100]
        # 또는 while문 사용
            # lista = [10, 20, 30, 40]
            # indexTemp = 0
            # while indexTemp < len(lista):
            #     lista[indexTemp] = 100
            #     indexTemp += 1
            # print(lista)



# 연습 문제
    # for a in list를 써서 v1의 값 모두 출력
        # v1 = list(range(10, 20))
        # for a in v1:
        #     print(a)
        # for a in range(0, len(v1)):
        #     print(v1[a])
        
# enumerate
# continue - 특정문을 만나면 다시 위 올라감

# 한 반에 수학점수가 60점 이상이면 합격, 60점 미만이면 불합격
# lista = [90, 25, 67, 45, 80]
# 위 리스트가 학생의 번호순대로 있을 때, 아래와 같이 출력하도록 코딩하여라
# "1번 학생은 합격입니다."
# "2번 학생은 불합격입니다."
    # 방법 1
        # a = 1
        # for h in range(5):
        #     if lista[h] >= 60:
        #         print(str(a) + "번 학생은 합격입니다.")
        #     else:
        #         print(str(a) + "번 학생은 불합격입니다.")
        #     a += 1
    # 방법 2
        # num = 1
        # for a in lista:
        #     if a >= 60:
        #         print("%d번째 학생은 합격입니다." % num)
        #     else: 
        #         print("%d번째 학생은 불합격입니다." % num)
        #     num += 1
    # 방법 3
        # for a in range(len(lista)):
        #     if lista[a] >= 60:
        #         print("%d 번째 학생은 합격입니다." % (a+1))
        #     else:
        #         print("%d 번째 학생은 불합격입니다." % (a+1))

# for문과 break: for문에서 break문을 반드시 써야 하는 상활
    # 연습문제 1
        # 혈액형이 a형인 고객 선착순 1명만 찾는 상황
        # lista = ['b','b','ab','a','b','a']
        # # 출력 결과: 4번째 고객이 이벤트에 당첨되었습니다.
        # answer = 0
        # for a in range(len(lista)):
        #     if lista[a] == 'a':
        #         answer = a + 1
        #         break
        # print(f"{a+1}번째 고객이 이벤트에 당첨되었습니다.")

# 구구단!  
    # 연습문제 - 5단 출력
        # for 문을 이용한 구구단
        # 구구단 5단을 출력해보자
            # for a in range(1, 10):
            #     print (f"5x{a} = {5 * a}")
            # >>  5x1 = 5
            #     5x2 = 10
            #     5x3 = 15
            #     5x4 = 20
            #     5x5 = 25
            #     5x6 = 30
            #     5x7 = 35
            #     5x8 = 40
            #     5x9 = 45
    # 연습문제 - while True 사용하여 구구단 input후 출력
        # "구구단 몇단을 계산해 드릴까요?" 물어본 뒤 구구단 출력
            # while True:
            #     a = int(input("구구단 몇단을 계산해 드릴까요?"))
            #     for b in range(1, 10):
            #         print(f"{a}x{b} = {a*b}")

# 이중 for 문
    # 구구단을 5단 - 9단까지 한꺼번에 출력
        # for a in range(5, 10):
        #     for b in range(1, 10):
        #         print(f"{a}x{b} = {a*b}")
# while + for
    # 구구단을 5단 - 9단까지 한꺼번에 출력
        # a = 5
        # while a < 10:
        #     for b in range(1, 10):
        #         print(f"{a}x{b} = {a*b}")
        #     a += 1

# lista = [10, 20, 30, 40]의 lista[0]과 lista[1]의 자리를 바꾸려면?
    # 방법 1
        # import copy
        # lista = [10, 20, 30, 40]
        # listb = copy.copy(lista)      # listb = copy.deepcopy(lista)
        # lista[0] = listb[1]
        # lista[1] = listb[0]
        # print(lista)
    # 방법 2
        # lista = [10, 20, 30, 40]
        # temp = lista[0]
        # lista[0] = listb[1]
        # lista[1] = temp
        # print(lista)
    # 파이썬에서 지원하고 있는 문법
        # lista[0], lista[1] = lista[1], lista[0]
        # print(lista)

# for문을 이용한 정렬 알고리즘
    # 리스트를 오름차순으로 정렬 - lista = [93, 45, 21, 30, 20, 94, 66, 71, 45]
        # .sort()
            # lista.sort()
            # print(lista)
            # >> [20, 21, 30, 45, 45, 66, 71, 93, 94]
        # 선택정렬 vs. 버블정렬
            # 선택정렬 select-sort - 0번째 index부터 가장 작은 값을 채워나가는 방식
                # lista = [93, 45, 21, 30, 20, 94, 66, 71, 45]
                # for a in range(len(lista)-1):                       # 첫번째 for문은 채워나가야 할 index를 의미
                #     for b in range(a+1, len(lista)):                # 두번째 for문은 비교의 대상이 되는 index를 의미
                #         if lista[a] > lista[b]:
                #             lista[a], lista[b] = lista[b], lista[a]
                #             b+=1
                # print(lista)
                # >> [20, 21, 30, 45, 45, 66, 71, 93, 94]
            # 버블정렬 bubble-sort
    # lista = [93, 45, 21, 30, 20, 94, 66, 71, 45]
    # a = 0

    # for a in range(len(lista)-1):
    #     print(lista)
    #     for b in range(a+1, len(lista)):
    #         if lista[a] > lista[b]:
    #             lista[a], lista[b] = lista[b], lista[a]
    #             a += 1
    #             print(lista)
    #         else:
    #             a = 0

    # print("finale:", lista)