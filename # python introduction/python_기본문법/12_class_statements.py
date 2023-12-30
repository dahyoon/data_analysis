# 나중에 13_module_import를 실행시키려면 이 파일의 이름을 12_class_statements.py 에서 class_statements.py로 바꿔야 됨!
# 이유: 파이썬 경우 파일명의 맨 처음 글자가 숫자여서는 안되기 때문.


# 클래스!
    # 객체를 정의해 놓은 것
    # 반복하여 사용하는 변수랑 함수를 미리 정해 놓은 틀


# 클래스의 사용
    # 1) 같은 기능의 함수의집합
        # 기본 구조: 
            # Class 클래스명:
            #     def 함수명1():
            #         return 
            #     def 함수명2():
            #         return 
            # print(Calculator.함수명n(변수))
    # 2) 객체 생성
        # 기본 구조:
            # class 클래스명:
                                            # __init__ 이란 '생성자'이다
                                            # 생성자는 객체생성될 때 객체변수를 초기화한다
            #     def __init__(self):       # 이 처음 두줄은 있으나 없으나 똑같은데 선언해주는 것이 좋음 (있으나 없으나 실행 됨)
            #         self.result = 0       #
            #     def plus(self, a):        # 함수 선언: 객체를 만들 때 메서드/클래스 내의 첫번째 매개변수(self)는 객체(aCompany, bCompany, etc.)를 의미한다
            #         self.result += 0
            #         return self.result    # 결과값 선언 - return 없어도 됨!
            #     def minus(self, a):
            #         self.result -= a
            #     def multiply(self, a):
            #         self.result *= a
            #     def divide(self, a):
            #         self.result /= a

# 사칙연산 함수가 있을 때, 같은 기능을 하므로 Calculator라는 클래스에 모아둘 수 있다
# 명명규칙
    # 대문자 알파벳으로 시작; camalcase 또는 _ 사용
    # 반대로 변수명, 함수명은 소문자로 시작; 또한 camalcase 또는 _ 사용


# 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태
        # class Calculator:
        #     def plus(a, b):
        #         return a + b
        #     def minus(a, b):
        #         return a - b
        #     def multiply(a, b):
        #         return a * b
        #     def divide(a, b):
        #         return a / b
        # print(Calculator.plus(10, 20))
        # >> 30
# 이 클래스의 문제점: 클래스 내에서 누적된 값을 변수로 갖고 있지 않음
        # class Calculator:
        #     result = 0
        #     # 클래스 변수 접근 방법
        #         # 1. 클래스명.변수 로 호출
        #         # 2. classmethod 데코레이터 사용
        #             # class 내에 선언 된 함수는 'method'라 부른다
        #     def plus(a):
        #         Calculator.result += a      # 1. 클래스명.변수 로 클래스 변수에 접근
        #     @classmethod                    # 2. classmethod 데코레이터 사용하여 클래스 변수에 접근 - @classmethod 쓴 다음 (cls-이름 상관 없음, 변수임)로 사용
        #     def minus(cls, a):
        #         cls.result -= a                     # 여기서 cls는 클래스명 (Calculator)을 가리킴
        #     def multiply(a):
        #         Calculator.result *= a
        #     def divide(a):
        #         Calculator.result /= a
        # print(Calculator.result)
        # Calculator.plus(10)
        # print(Calculator.result)
        # Calculator.minus(5)
        # print(Calculator.result)
        # >>  0
        #     10
        #     5


# 객체란 클래스의 '복제본'이며 '인스턴스'라 부르기도 한다
# 객체의 사용 이유
    # 클래스의 중복 제거 -> 변수와 함수의 재활용의 어려움 해결!
# 객체 형식의 클래스(객체를 만들기 위한 클래스)의 기본 구조
        # class Calculator:
        #     # 객체가 생성될 때 init은 가장 먼저 실행
        #     def __init__(self):
        #         self.result = 0
        #     def plus(self, result):      # 객체를 만들 때 메서드/클래스 내의 첫번째 매개변수(self)는 객체(aCompany, bCompany, etc.)를 의미한다
        #         self.result += result    # result와 self.result는 다른 값이다
        #     def minus(self, result):
        #         self.result -= result
        #     def multiply(self, result):
        #         self.result *= result
        #     def divide(self, result):
        #         self.result /= result
        # aCompany = Calculator()           # 객체 만들기
        # aCompany.plus(100)
        # bCompany = Calculator()
        # bCompany.plus(100)
        # print(aCompany.result)
        # print(bCompany.result)
    # 특이점: return이 없음 - 이유: 메모리 상 객체는 힙메모리에 저장이 돼서 밖에서 쓸 수 있기 때문에 return이 없어도 된다; return이 있어도 된다
# 클래스 생성 시 매개변수를 통해 초기값 세팅가능
        # class Calculator:
        #     def __init__(self, a):
        #         self.result = a
        #     def plus(self, result):     
        #         self.result += result
        #     def minus(self, result):
        #         self.result -= result
        #     def multiply(self, result):
        #         self.result *= result
        #     def divide(self, result):
        #         self.result /= result
        # aCompany = Calculator(1000)       # 객체 만들기
        # print(aCompany.result)
        # bCompany = Calculator(2000)
        # print(bCompany.result)

# 연습문제!
    # Person이라는 클래스를 만든다.
    # 생성자로 이름(name), 나이(age), 성별(gender), email이라는 매개변수를 받아 각각의 객체변수를 만든다.
    # register이라는 메서드를 만들어서 해당 메서드에서는 myInfo라는 객체변수에 이름, 나이, 성별, 이메일 정보를 문자열로 담는다.
    # 2명의 person을 만든다.
    # 호출: p1.register()
    #      print(p1.myInfo)
    #      print(p2.myInfo)

    # 방법 1) init할 때 초기화 하는 경우; 보통 init에서 초기화를 한다
        # import datetime
        # class Person:
        #     def __init__(self, name, age, gender, email):       # init할 때 초기화 하는 경우; 보통 init에서 초기화를 한다
        #         self.name = name
        #         self.age = age
        #         self.gender = gender
        #         self.email = email
        #         self.regDate = str(datetime.datetime.now())     # 사용자의 입력 필요하지 않다
        #     def register(self):                                 # 여기서 매개변수 받아도 되나, 힙메모리에 저장 되어 있기 때문에 꼭 매개변수를 안 써줘도 된다
        #         self.myInfo = self.name + ", " + self.age + ", " + self.gender + ", " + self.email + ", " + self.regDate

        # p1 = Person('ho', '19', '남', 'ho@naver.com')
        # p2 = Person('goo', '34', '여', 'goo@naver.com')
        # p1.register()
        # p2.register()
        # print(p1.myInfo)
        # print(p2.myInfo)
        # >> ho, 19, 남, ho@naver.com, 2023-05-31 12:11:53.587280
        #    goo, 34, 여, goo@naver.com, 2023-05-31 12:11:53.587298
    # 방법 2) #   register할 때 초기화 하는 경우
        # class Person:
        #     def register(self, name, age, gender, email):         #   register할 때 초기화 하는 경우
        #         self.myInfo = name + ", " + age + ", " + gender + ", " + email 
        # p1 = Person()
        # p2 = Person()
        # p1.register('ho', '19', '남', 'ho@naver.com')
        # p2.register('goo', '34', '여', 'goo@naver.com')
        # print(p1.myInfo)
        # print(p2.myInfo)
        # >> ho, 19, 남, ho@naver.com
        #    goo, 34, 여, goo@naver.com

# 현재시간 출력하기
    # import datetime
    # print(datetime.datetime.now())

# 클래스의 상속
    # 부모 클래스에서의 기능을 자식클래스에서 물려받는 것
    # class 자식클래스명(부모클래스명) 형식으로 선언

class Calculator:
    def __init__(self):
        self.result = 0
    def plus(self, a):      # 객체를 만들 때 메서드/클래스 내의 첫번째 매개변수(self)는 객체(aCompany, bCompany, etc.)를 의미한다
        self.result += a    # result와 self.result는 다른 값이다
    def minus(self, a):
        self.result -= a
    def multiply(self, a):
        self.result *= a

class CalculatorChild(Calculator):      # CalculatorChild는 Calculator의 모든 것을 상속
    pass

# CalculatorChild가 Calculator의 모든 것을 상속하고 난 후 추가/overriding(덮어쓰기)할 수 있다
class CalculatorChild(Calculator):
    def divide(self, a):
        self.result /= a
    def multiply(self, a):              # 부모한테 있는 기능을 재선언하게 되면, 부모의 기능보다 자싱의 기능이 우선시되고 이를 overriding(재정의)이라 한다 (__init__ 도 overriding 하면 됨)
        self.result *= (a+1)            # overloading이라는 개념도 다른 언어에는 있는데 파이썬에서는 기본구성에 있지 않다

if __name__ == "__main__":              # 자신이 실행 할 때에는 자신이 main이니까 실행, 그러나 다른 코드에서 사용할 때에는 이 if 아래에 있는 코드를 사용하지 않는다
    print(__name__)                     # >> __main__

if __name__ == "__main__":              # 자신이 실행 할 때에는 자신이 main이니까 실행, 그러나 다른 코드에서 사용할 때에는 이 if 아래에 있는 코드를 사용하지 않는다
    cc1 = CalculatorChild()
    cc1.plus(100)
    print(cc1.result)
# print(cc1)      # >> 메모리 주소 출력
# print함수가 속해있는 클래스는 object클래스를 상속 받고 있다.
# 그런데, object클래스 안에는 list, dict같은 파이썬에서 자주 사용되는 객체값을 value형식으로 출력해주는 함수가 내장돼있다.