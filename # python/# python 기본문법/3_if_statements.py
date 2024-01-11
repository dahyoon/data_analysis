# if문의 기본 구조
# (else는 optional 요소)
#   if 참 조건:
#       실행문
#   else:
#       실행문
# 예)
    # a = int(input("a는 무슨 숫자입니까?"))
    # if a>10:
    #     print("a는 10보다 큽니다.")
    # else: 
    #     print("a는 10보다 작습니다.")

    # trueOrFalse = True
    # if trueOrFalse:
    #     print("참입니다.")
    # else:
    #     print("거짓입니다.")

    # money = int(input("얼마를 가지고 있습니까?"))
    # if money > 30000:
    #     print("택시를 타고 가시오.")
    # else:
    #     print("걸어가시오.")

# pass
    # pass를 명시적으로 표현해준 것
        # a = input("결제 수단을 입력해주세요.")
        # m1 = ['card', 'cash']
        # if a in m1:
        #     pass
        # else:
        #     print("결제 방법이 잘못되었습니다.")

# 비트연산이란 2진법의 숫자를 |(or), &(and), ^(xor) 등으로 CPU 내부적으로 계산하는 방식
    # a = 10
    # if (a > 5) | (a > 100):       # 반드시 () 해줘야 됨
    #     print("참입니다.")
    # >> 참입니다.
    # if a > 5 or a > 100:
    #     print("참입니다.")
    # >> 참입니다.

    # and는 &, or는 |, not은 부정의 의미
    # 비트연산을 할 때에는 기호를 써야 된다 (and, or, not이 아니라 - 조금 다른 방식/의미로 쓰임)
    # not True는 False, not False는 True

    # 1111 & 1000 => 1000
    # 1111 | 1000 => 1111

# 대입 연산자
    # += -= /= *= 
    # a = 10
    # a += 1        # a = a + 1 과 동일
    # print(a)
    # >> 11
    # print(a += 1)
    # >> SyntaxError: invalid syntax

# 비교 연산자
    # chaining (범위 표현 가능, 몇 다른 언어에서는 표현 불가능)
        # 5 < a < 100       # a > 5 and 100 < a 와 동일
            # a = 10
            # if 5 < a < 100:
            #     print("참입니다.")
            # >> 참입니다.

# 조건부표현식(삼항 연산자) - 간단한 식으로 표현
    # 먼저, if문의 실행문을 if문 앞으로, ':'을 빼고 한줄로 표현
    # 실행문을 실행하기 위한 사용 보단 참인 경우 어떤 값, 거짓인 경우 어떤값을 쉽게 result에 담기 위해 사용
        # a = 10
        # print("a는 10보다 큽니다.") if a > 10 else print("a는 10보다 작습니다.")
        # >> a는 10보다 작습니다.
        # result = 'a는 10보다 큼' if a > 10 else 'a는 10보다 작음'
        # print(result)
        # >> a는 10보다 작음

# if문 한 줄로 쓰기
    # 코드가 짧고 단순한 경우에 아래와 같이 한줄로 쓰기 권장
    # 두줄 이상의 코드를 한줄로 적고 싶으면 ; 로 구분
        # a = 10
        # if a > 1: print("a는 1보다 큽니다"); print("a는 1보다 큽니다..!")
        # >> a는 1보다 큽니다
        #    a는 1보다 큽니다..!

# f formating
    # {} 안에 변수값이 들어감
        # print(f"짐의 무게는 {weight}kg이며 수수료는 {cost}입니다.")

# is 연산자
    # if a is b:
    #   실행문    

    # a 와 b가 같은지 비교하는 연산자 is
    # 객체타입의 경우 메모리 주소를 비교; lista 와 listb 가 같더라도 비교해보면 메모리 주소가 다르기에 False
        # a = [1, 2]
        # b = [1, 2]
        # if a is b:
        #     print("참")
        # else:
        #     print("거짓")
        # >> 거짓
    # 숫자, 문자, bool 기본타입의 경우 값을 비교; 이들은 비교할 때 메모리 주소가 아닌 데이터 pool을 만들어서 재활용함; 값을 데이터 pool에서 비교
        # a = 3
        # b = 3
        # if a is b:
        #     print("참")
        # else:
        #     print("거짓")
        # >> 참

# 연습문제
    # 항공사에서는 짐을 부칠 때 10kg 이상부터 수수료를 낸다. 
    # 수수료는 10의 배수 단위로 10000원씩 증가한다. 
    # 만약 10kg 미만이면 수수료는 없다.
    # 사용자의 짐의 무게를 키보드로 입력 받고, 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하라.
    # 결과화면 예시
    # 짐의 무게는 얼마입니까? 21
    # 짐의 무게는 21kg이며 수수료는 20000입니다.
        # weight = float(input("짐의 무게는 얼마입니까?"))
        # if weight < 1:
        #     cost = 0
        # else:
        #     cost = weight//10 * 10000
        # answer = "짐의 무게는 %fkg이며 수수료는 %d입니다." % (weight, cost)
        # print(answer)

# 연습문제
    # 돈이 만원 이상 있고 배가 고프면 "저녁을 사먹으시오" 출력
    # 그렇지 않으면 "집에 가시오" 출력
    # input값으로 가진 돈과 배가 고픈지 여부를 받아서 처리
        # money = int(input("돈이 얼마 있습니까?"))
        # hungryOrNot = input("배가 고프십니까? 응 또는 아니로 대답해주세요.")
        # if money >= 10000 and hungryOrNot == '응':
        #     print("저녁을 사먹으시오.")
        # else:
        #     print("집에 가세요.")