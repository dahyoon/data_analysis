# 예외처리: try except 구문
# 예외처리하는 이유: 프로그램실행 중 예외가 발생하더라도 프로그램이 강제종료 되지 않도록 하기 위함

while True:
    # 분자를 입력해주세요 first
    # 분모를 입력해주세요 second
    # 문제/error 가능 부분에 try - 가능한 문제: 사용자가 숫자가 아닌 str을 입력했을 때
    try:  
        first = int(input("분자를 입력해주세요."))
        second = int(input("분모를 입력해주세요."))
    # 또한, 사용자가 0으로 숫자를 나누게 되면 division by zero error가 발생하게 된다
        print(first/second)
    # 문제/error 났을 때 이후의 action except       # 이렇게 try except구문을 사용하여 프로그램을 강제종료 시키지 않고 진행할 수 있도록 한다
    except ZeroDivisionError as zd:             # error난 것이 어떤 error인지 순차적으로 위에서부터 확인하면서 자신이 해당하는 error에 print함
        print(f"{zd} 오류입니다.")
    except ValueError as ve:
        print(f"{ve} 오류입니다.")
    except Exception:                           # 이 Exception은 모든 exception들을 포함하는 것으로, 이 구문이 except 중 가장 위에 있으면 모든 error가 이 print로 출력된다.
        print(f"{Exception} 오류입니다.")
    # finally는 문제가 있든 없든 무조건 실행 (있어도 되고 없어도 됨: optional)
    finally:
        print("결과를 확인해주세요.")


# Error 강제의 예시
    # while True:
    #     raise Exception     # Error를 여기서 강제로 발생시킨 것

# 부모클래스 raise Exception(에러 강제)를 통해 자식클래스로 하여금 overriding(재정의) 유도
    # class Bird:
    #     def fly(self):
    #         raise Exception

    # class Eagle(Bird):
    #     def fly(self):
    #         print("fly fly")

    # eagle1 = Eagle()
    # eagle1.fly()
    # >> fly fly