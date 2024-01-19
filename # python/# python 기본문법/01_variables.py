# 교제추천
# - 점프 투 파이썬 (온라인 무료, 강사 추천)
# - TCP School

# 프로그램 다운로드시 
# MacBook Air (M1, 2020)
# Chip Apple M1 --> ARM, Apple Chip, 등으로 표기되어 있는 것으로 다운로드

# 주석
    # # 표시는 프로그래밍에서 주석이라 말한다.
    # 주석은 파이썬의 인터프이터가 인식하지 못하도록 쓰는 기호
    # Ctrl + /

# print()
    # 코드 실행 후 결과값을 가시적으로 보여주기 위해 터미널 창에 출력하는 것

# input()
    # return 값은 strings

# True False
    # 숫자: 0 - False; 0이 아닌 모든 숫자 - True
    # 문자열: 빈 문자열 - False; 아무 문자열 - True
    # 다른 형태 (리스트, 셋, 딕셔녀리 등등)들도 문자열과 동일

# a = 1
    # 의미: a와 1이 같다라는 의미가 아니라, a라는 이름의 변수에 1을 담겠다는 뜻이다.
    # b = '1'

# a = a + 1
    # 의미: '새로운 a' 값에 "'원래 a' 값 더하기 1" 값을 넣겠다는 뜻이다

# 변수 자료형 출력해보기  
    # a = 1
    # print(type(a))
    # >> <class 'int'>

    # b = True
    # print(type(b))
    # >> <class 'bool'>

    # c = 2.3
    # print(type(c))
    # >> <class 'float'>

# 문자 자료형 출력해보기
    # x = "a"
    # print(ord(x))
    # >> 97
    # y = "A"
    # print(ord(y))
    # >> 65

# """   """ 쌍따음표/홑따음표 3개
    # multi line으로 문자열을 표현
    # 예) a = """hello

    # world"""
    # print(a)
    # >> hello

    #    world

# * --> all을 의미 (곱하기 외에도 다른 의미가 있음!)


# \n 또는 \t - 이스케이프문을 활용한 줄바꿈
    # 이스케이프문이란 \n (줄바꿈) 또는 \t (tap키) 등의 특수기호를 말한다.
    # a = "hello\nworld"
    # print(a)
    # >> hello
    #    world
    # a = "hello\tworld"
    # print(a)
    # >> hello
    #    world

# \역슬래시(won doller 포함)의 또다른 활용 - 특수문자를 있는 그대로 표현
    # a = "쌍따음표(\")는 파이썬에서 문자를 의미한다"
    # print(a)
    # >> 쌍따음표(")는 파이썬에서 문자를 의미한다
    # a = "\'"
    # print(a)
    # >> '
    # a = "\\"
    # print(a)
    # >> \
# % 를 넣고 싶은 경우 안 될 때
    # %% - 두 개 넣는다

# 문자열 곱하기, 더하기
    # a = "Python is fun." 
    # b = "Bye."
    # c = a * 2 + b
    # print(c)
    # >> Python is fun.Python is fun.Bye.

# 문자열 index
    # str[] - 자리 순서: 0, 1, 2, 3, 4, 5 ...
        # st = "python's fun"
        # print(st[3])
        # >> h
    # str[-1] - 마지막문자를 출력: 자리 순서: ... -3, -2, -1
        # st = "python's fun"
        # print(st[-1])
        # >> n

# len() - 문자열 길이 구하기
    # st = "hello"
    # print(len(st))
    # >> 5

# 문자열의 슬라이싱 - 슬라이싱이란 문자열을 잘라내는 것
    # st[x:y] - x이상 y미만의 index를 가진 문자열을 잘라낸다
        # a = "python is fun"
        # python만 잘라내서 b에 담아 출력
        # b = a[0:6]
        # print(b)
        # >> python

    # x, y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
        # a = "python is fun"
        # 6번째 문자부터 끝까지 잘라내서 변수 b에 담아 출력
        # b = a[6:]
        # print(b)
        # >> is fun
    # st[x:y:z] 여기에서 z는 z-1 개씩 건너뛰고
        # a = "python is fun"
        # 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
        # print(a[2:7:2])
        # >> to
            # 연습문제(슬라이싱)
            # a = '20220505children's_day' 슬라이싱을 이용하여 date라는 변수에 날짜, day라는 변수에 children's_day을 담아서 각각 출력(print)
            # a = '20220505children\'s_day'
            # date = a[0:8]
            # day = a[8:]
            # print(date)
            # >> 20220505
            # print(day)
            # >> children's_day

# str으로 끝나는지 확인
    # print('Hello'.endswith('llo'))
    # >> True
# str으로 시작하는지 확인
    # pring('Hello'.startswith('He'))
    # >> True

# 문자열 포맷팅 - 문자열 중간에 특정 문자 (또는 숫자 등)를 삽입하는 방식
    # 목적: 문자열을 직접 삽입하면 1회성으로 coding할 수 밖에 없지만, 포맷팅은 변수값을 삽입할 수 있다; 따움표를 여러번 안 닫아도 된다
        # 아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이 해서 귀찮다
        # a = "I studied " + language + " very hard " + times + " times."
        # print(a)
    # 종류: %s - 문자열; %d - 정수 (d = decimal); %f - 실수

# 정보 입력 요구
    # input()
        # input()의 return 값은 항상 str(문자) 값이 된다
        # 그러므로 input()에 입력하는 str을 %d나 %f로 형변환 시켜줘야 된다 -> int(str) 아니면 float(str)
        # 예)
            # language = input("좋아하는 언어를 입력하세요.")
                # 이때 language의 class는 string
            # times = input("그 언어를 몇 번이나 공부하셨나요?")
                # 이때 times의 class는 string
            # a = "I studeid %s very hard %d times." % (language, int(times))
            # print(a)

    # 연습문제
        # 나이가 몇 살이신가요? 해서 나이를 받고, 몸무게가 몇 킬로그램이신가요? 해서 weight 받고, My age is %d, and weight is %f kg
        # 위 문자열을 포맷팅을 통해 사용자의 입력값에 따라 달라지도록 만들고 그 결과값을 출력
        # age = input("나이가 몇 살이신가요?")
        # age = int(input("나이가 몇 살이신가요?")) <- 여기다가 정수변환 해도 됨
        # weight = input("몸무게가 몇 킬로그램이신가요?")
        # weight = float(input("몸무게가 몇 킬로그램이신가요?")) <- 여기다가 실수변환 해도 됨
        # a = "My age is %d, and weight is %f kg." % (int(age), float(weight))
        # print(a)

# 문자열 세기
    # str.count('o') - 대상 문자열/리스트/튜플에 지정한 문자가 몇개가 있는지 출력하는 함수
        # a = "python"
        # print(a.count('o'))
        # >> 1
    # set이랑 dict는 카운트 못함

# 문자열 순서 찾기 (index)
    # str.find('o') str.index('o') - 대상 문자열에 지정한 문자가 몇 번째 index에 있는지 출력하는 함수
        # a = "python"
        # print(a.find('o'))
        # >> 4
        # print(a.index('o'))
        # >> 4
    # 없는 문자를 찾을 때에는 -1 return한다
        # a = "python"
        # print(a.find('x'))
        # >> -1
    # st.rfind('o') - 대상 문자열에 지정한 문자가 몇 번째 index에 **마지막**으로 있는지 출력하는 함수
        # a = "hello"
        # print(a.rfind('l'))
        # >> 3
# 연습
        # whatyouwant = input("아무런 문자나 입혁해주세요")
        # search = input("찾고자 하는 문자 1개만 입력해주세요")
        # result = whatyouwant.find(search)
        # if result == -1:
            # print("찾고자 하는 값이 없습니다.")
        # else:
            # print("요청하신 문자는 %d 번째에 있습니다." % result)

# 열 종류 확인
    # 열.isnumeric() - 열이 숫자(정수, 실수 다 포함)인지 아닌지 확인 (True/False)
    # 열.isdigit() - 열이 문자열인지 아닌지 확인 (True/False)

# 문자열 대소문자 변경
    # str.upper() / str.lower()
        # a = "hello"
        # print(a.upper())
        # >> HELLO
        # b = "HELLO"
        # print(a.lower())
        # >> hello
    # str.swapcase()
        # a = 'DeeesEEEo'
        # print(a)
        # >> dEEEseeeO

# 문자열 양쪽 공백을 없애기
    # st.strip()
        # a = "     hello world      "
        # print(a.strip())
        # >> hello world
    # str.strip(' \n$#%')
        # a = "    Hello I'm Pearl, I have $500 dollars #I'm rich.  \n  $%#"
        # print.(a.strip(' \n$#%'))
        # >> Hello I'm Pearl, I have $500 dollars #I'm rich.

# myId = (input("id를 입력해주세요")).strip()
# myPw = input("비밀번호를 입력해주세요")
# print("ID는 " + myId + "이고 " + "비밀번호는 " + myPw + "입니다.")

# 문자열 대체
    # st.replace() 수정 안하고 불러오기만 함
        # a = "I studied python."
        # print(a.replace("python", "java"))
        # >> I studied java.

# 문자열 쪼개기
    # str.split() - 공백을 기준으로 문자를 잘라서 리스트에 넣음
        # a = "I studied python."
        # b = a.split()
        # print(b)
        # >> ['I', 'studied', 'python.']
        # a = "I     studied      python."
        # b = a.split()
        # >> ['I', 'studied', 'python.']
    # str.split(':') - ':'을 기준으로 문자를 잘라서 리스트에 넣음
        # a = "I:studied:python."
        # b = a.split(":")
        # print(b) 
        # >> ['I', 'studied', 'python.']

# 제곱
    # pow(x, y) - x의 y 거듭제곱 (x의 y승) 반환
        # 먼저 import math 해야됨
        # 다음 math.pow(x, y)

# 제곱근
    # sqrt(x) - x의 제곱근 (x에 루트를 씌운 값) 반환
        # 먼저 import math 해야됨
        # 다음 math.sqrt(x)

# 연습문제(숫자형)_교제
    # 아래와 같은 2차 방정식을 파이썬 수식으로 코딩하고 y의 결과를 출력
    # y = 2.5 * x^2 + 3.3 * x + 6
        # x = int(input("x값을 입력해주세요."))
        # y = 2.5 * pow(x, 2) + 3.3 * x+ 6
        # print(y)

# 3개의 단어를 키보드로 입력 받아 각 단어의 첫글자를 추출 후 단어의 약자를 출력
# <조건1> 각 단어 변수 (word1, word2, word3)
# <조건2> 입력과 출력 구분선: 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
# word1 = input("첫번째 단어를 입력해주세요.")
# word2 = input("두번째 단어를 입력해주세요.")
# word3 = input("세번째 단어를 입력해주세요.")
# print(word1[0] + word2[0] + word3[0]) 
# >> Korea, Busan, Kangnam 라고 입력했을 때 >> KBK


# 2진수
    # bin(int) - 10진수 int을 2진수 문자열로 변환
        # print(bin(2))
        # >> 0b10
    # int('2진수 문자열', 2) - 2진수 문자열을 10진수 문자열로 변환
        # print(int('10', 2))
        # >> 2

# range 문법
    # range(x, y) - x 이상 y 미만의 숫자를 담은 객체
    # range(y) - 0 이상 y 미만의 숫자를 담은 객체
    # iterable한 객체 -> list로 변환 가능
    # range를 list로 바꾸기 - list()
        # v1 = list(range(1, 5))
        # print(v1)
        # >> [1, 2, 3, 4]
    # 이 때, range 안에 있느 값은 int
        # for a in range(1):
            # print(type(a))
            # >> <class 'int'>

# enumerate
    # 인덱스(index)와 원소(element)를 튜플(tuple) 형태로 만들어준다
    # for a, b in enumerate(['a', 'b', 'c']):
    #     print(a, b)
    # >> 0 a
    # >> 1 b
    # >> 2 c

# * -> unpacking parameter
    # 예) def hello(*arg):
            # ...
        # 이 때 *는 곱하기가 아니라 unpacking parameter가 된다

# %%
