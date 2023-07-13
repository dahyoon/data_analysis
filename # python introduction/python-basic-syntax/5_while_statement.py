# while문 - 조건문이 참인 경우 반복; 무한반복이 기본전제
    # 조건을 확인 후 True이면 실행문을 1회 실행시키고 다시 조건을 확인하러 돌아온다.
    # 그리고 True이면 또 다기 실행한다.
    # 그러다 조건이 False가 되면 while문 종료

# 기본구조
    # listA = [1, 2, 3]
    # while listA:
        # print("참입니다.")
        # >> 무한반복!!!

# 외우기 (많이 나오는 구조))
    # a = 0
    # while a < n: << True면 반복, False면 스톱
    #     실행문
    #     a += 1

#무한반복 멈추기
    # Ctrl + C - 프로그램을 멈춤
    # 조건 걸어주기
        # a = 0
        # while a < 5:
        #     print(str(a) + "번 무한반복")
        #     a += 1                            # 조건!
        # >>  0번 무한반복
        #     1번 무한반복
        #     2번 무한반복
        #     3번 무한반복
        #     4번 무한반복
    # .pop()   --> 원래 리스트 수정 (str, tuple, dict 안 됨)
        # listA = [1, 2, 3]
        # while listA:
        #    print("참입니다.")
        #    listA.pop()
        # >> 참입니다.
        #    참입니다.
        #    참입니다.
    # break
        # if문을 써서 어떠한 조건에 break
# continue - 이 구문을 만나면, 다시 반복문 조건으로 이동


# 랜덤의 값을 추출하는 파이썬 라이브러리 -> random
    # import random
    # print(random.randint(1, 45))   --> 1이상 45 이하
    # >> 26

# 연습 문제
    # 1 - 1000까지 출력
        # a = 1
        # while a < 1001:
        #     print(str(a) + "번 무한반복")
        #     a += 1
    # 1-1000까지 모두 더한 값과 평균 출력
        # sum = 0
        # a = 1
        # while a < 1001:
        #     sum += a
        #     a += 1
        # print(sum, sum/1000)
        # >> 500500 500.5
    # 위 문제를 while문에서 반복 진행하다가 if문 써서 어떠한 조건에서 break
        # a = 1
        # sum = 0
        # while True:
        #     sum += a
        #     a += 1
        #     if a == 1001:
        #         break
        # print(sum)
        # >> 500500
    # 1-1000 중 홀수만 더해서 출력
        # 방법 1
            # a = 0
            # sum = 0
            # while a < 1000:
            #     a += 1
            #     if a%2 != 0:
            #         sum += a
            # print(sum)
            # >> 250000
        # 방법 2
            # lista = []
            # for a in range(1, 1001):
            #     lista.append(a)
            # for a in range(len(lista)):
            #     answer = sum(lista[::2])
            # print(answer)
            # >> 250000
    # 위 문제를 continue 활영해서 출력
        # sum = 0
        # a = 0
        # while a < 1000:
        #     a += 1
        #     if a%2 == 0:
        #         continue
        #     sum += a
        # print(sum)
        # >> 250000
    # 각도 검사기
        # while True:
        #     num1 = int(input("1-180까지 입력해주세요."))
        #     if num1 > 180:          
        #         print("잘못된 값입니다.")
        #         continue          # 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 해준다(검수 불필요한 값을 앞에서 걸러버린다)
        #     elif num1 < 90:
        #         print("예각입니다.")
        #     elif 90 == num1:
        #         print("정각입니다.")
        #     elif 90 < num1 < 180:
        #         print("둔각입니다.")
        #     elif num1 == 180:
        #         print("평각입니다.")
    # 나만의 리스트 만들기
        # 리스트의 크기를 키보드로 입력받아 그 크기만큼 임의 숫자를 리스트에 추가하고, 리스트의 크기와 값 전체를 출력하라.
        # 모든 값은 키보드로 입력을 받고, list의 크기 len() 함수를 통해 구하라. 단, 리스트의 크기는 10 이하로 입력하라
        # 출력화면 예)
            # 리스트의 크기를 정하세요. 30
            # 리스트의 크기를 10 이하로 다시 할당하세요. 9
            # 리스트에 값을 할당해 보세요. 1
            # 리스트에 값을 할당해 보세요. 2
            # 리스트에 값을 할당해 보세요. 9
            # 크기9의 리스트 ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 가 할당 되었어요
        # 선생님 방법
            # while True:
            #     listSize = int(input("리스트의 크기를 10 이하로 입력하세요."))
            #     if listSize <= 10:
            #         a = 0
            #         lista = []
            #         while a < listSize:
            #             listvalue = input("리스트에 값을 할당해 보세요.")
            #             lista.append(listvalue)
            #             a += 1
            #         print(lista)
            #     else:
            #         print("입력하신 숫자가 10을 초과합니다.")
        # 내 방법
            # while True:
            #     list = []
            #     listSize = int(input("리스트의 크기를 10 이하로 입력하세요."))
            #     if listSize > 10:
            #         print("입력하신 숫자가 10을 초과합니다.")
            #         continue
            #     else:
            #         for a in range(1, listSize+1):
            #             if a <= listSize:
            #                 listvalue = input("리스트에 값을 할당해 보세요.")
            #                 list.append(listvalue)
            #         a = f"크기 {listSize}의 리스트 {list}가 할당 되었어요."
            #         print(a)
    # 로또 번호 생성기
        # 리스트의 크기가 6개인 리스트를 만들어서 오늘의 로또번호를 만들어보자
            # import random
            # print(random.randint(1, 45))
            # a = 1
            # list = []
            # while a <= 6:
            #     list.append(random.randint(1, 45))
            #     a += 1
            # print(list)
# 최대값, 최소값 구하기
    # 1-100의 정수 중 10개를 뽑아 리스트로 담고 최대값과 최소값을 구하라


        # import random
        # lista = []
        # while len(lista) < 10:
        #     lista.append(random.randint(1,100))
        # lista.sort()
        # max = lista[-1]
        # min = lista[0]
        # print(f"Random numbers are {lista}, and the maximum number is {max} while the minimum is {min}.")

# continue
# break