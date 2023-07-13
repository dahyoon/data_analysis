# a = 3
# b = 4
# '3'와 '4'는 정수, '0.75'는 실수
# 파이썬은 정수를 가지고 계산해서 실수 값이 나와도 자동적으로 실수 값을 나타내줌 (다른 언어들은 오류나는 경우 있음)
# 몫: //, 나머지: %
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

# 자료의 형변환
    # a = 10
    # b = 20
    # 결과값이 1020이 나오도록 덧셈을 하여라
        # print(str(a) + str(b))
    # c = 2.333333
    # d = 5/4
    # c와 d의 소수부분을 잘라서 출력하라
        # print(int(c))
        # print(int(d))

# 제곱, 제곱근
# 2의 10 제곱을 출력하라
    # print(2**10)
    # print(pow(2,10))
# 제곱근은 math라는 라이브러리를 import해줘야 한다.
    # import math
# 위는 math라는 라이브러리를 선언하는 것
# pow(a,b) 또한 math 라이브러리에도 있다
    # print(math.pow(2,10))
# 1024의 제곱근을 구하라
    # print(math.sqrt(1024))

# 확률조합 (num1) Combinations of (num2)
    # (num1)C(num2) --> (num1)! / (num2)! * (num1-num2)!
    # 5! = 5*4*3*2*1
    # 3! = 3*2*1
    # 예시 문제:
        # 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 
        # 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
        # balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
            # 입출력 예
                # balls = 3; share = 2; result = 3
                # balls = 5; share = 3; result = 10
        # <Note> balls! / share! * (balls - share)!
            # num1 = 1
            # num2 = 1
            # num3 = 1
            # for a in range(1,(balls+1)):
            #     num1 *= a
            #     print("base is:", num1)
            # for b in range(1, (share+1)):
            #     num2 *= b
            #     print("share is:", num2)
            # for c in range(1, (balls - share + 1)):
            #     num3 *= c
            #     print("remainder is:", num3)
            # answer = num1/(num2*num3)
            # print(int(answer))



# while True:
#     gugu = int(input('please enter number: '))
#     for a in range(1, 10):
#         print(f"{gugu} X {a} = {gugu*a}")