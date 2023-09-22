
# 특정한 input값이 있을 때, 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자
# 그런데, 해당 연산은 매우 빈번하게 사용이 된다고 가정하자
# 복잡한 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자
# 옵션: input 과 return 값이 있거나 없어도 됨
    # input과 return 있는 경우
        # def myFunc(myInput):                                    # def 함수명(매개변수):            # 예)
        #     calc = (((myInput + 10) * 20) / 10) ** 2            #   실행문                       #     max()
        #     return calc                                         #   return 결과값                #     min() 
    # input과 return 없는 경우                                       # def 함수명():                  # 예)
        # def hello():                                            #    실행문                      #    .sort()  
        #     print("hello")
# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출
# 연습!
    # 함수명: myPlusFunc; 함수의 로직: 사용자의 input을 받아 input값의 누적합을 더하는 함수
    # 예) 100을 입력하면 1+2+3+...+100 의 값을 구하는 함수
        # def myPlusFunc(num):
        #     return sum(list(range(1, num+1)))
    # input값 2개를 받아 2값을 더한 뒤, *2만큼 하여 return하는 함수
    # 그리고, 해당 함수를 호출하여 호출된 결과값은 result에 담아 출력
        # def sumTimesTwo(num1, num2):
        #     return (num1 + num2)*2

# 연습문제 풀기 (아래)

# list의 index함수를 쓰지 않고 for문 또는 while문을 통해 숫자 9가 몇번째 index에 있는 값인지 print보자 
    # .index() 쓰기
        # lista = [1, 4, 6, 9]
        # print(lista.index(9))
    # while 쓰기
        # lista = [1, 4, 6, 9]
        # a = 0
        # while a < len(lista):
        #     if lista[a] == 9:
        #         print(a)
        #         break
        #     else:
        #         a += 1
    # for 쓰기
        # lista = [1, 4, 6, 9]
        # for a in range(len(lista)):
        #     if lista[a] == 9:
        #         print(a)
        #         break                 # break를 넣어줘야 가장 첫 9의 인덱스만 출력: break 안 걸 시 뒤에 있는 9의 인덱스도 출력
    # 위의 for/while문을 활용하여 myIndex라는 이름의 함수 만들기, input 값 2개(list, 변수); print는 함수 내에서 하지 않고 return에 값을 담는다
        # def myIndex(lista, num):
        #     result = "없어요"
        #     for a in range(len(lista)):
        #         if lista[a] == num:
        #             result = a
                            # break 할 필요 없이, 바로 return을 해도 된다. (if문의 종속문으로)
                            # return을 하게 되면 함수 전체가 강제종료 된다.
        #             break 
        #     return result
        # print(myIndex([1, 2, 9, 4], 9))

# 사용자 정의 함수
    # 키보드로 반지름의 길이를 입력받고 원의 넓이를 구하는 함수를 만들어 결과 출력
    # 원의 넓이 = 반지름 * 반지름 * 3.14
        # def circleSize(num1):
        #     circleSize = num1 ** 2 * 3.14
        #     return circleSize
        # num1 = int(input("반지름의 길이를 입력하세요."))
        # circleSize(num1)
        # print("원의 넓이 : " + str(circleSize(num1)))
        # >> # input값이 3일 때 원의 넓이는 28.26
# 입력 값이 없는 함수
    # "hello python!"
        # hello1() 이렇게만 호출했을 때 "hello1 python!" 출력하는 함수
            # def hello1():
            #     print("hello1 python!")

            # hello1())
            # >> hello1 python!
            # print(hello1())
            # >> None   # return 값이 없기 때문이다
        # print(hello2())라고 실행했을 때 "hello2 python!" 출력하는 함수
            # def hello2():
            #     return "hello2 python!"

            # print(hello2())
            # >> hello2 python!
# 입력값의 개수가 정해져 있지 않고 multiple한 함수
        # def sum(*args):
        #     total = 0
        #     for a in args:
        #         total += a
        #     return total

        # totalValue = sum(1,2,3,4,5)
        # print(totalValue)
# 2개 이상의 return값이 있는 경우
        # def cal(a, b):
        #     result1 = a + b
        #     result2 = a - b
        #     result3 = a * b
        #     return result1, result2, result3

        # calValue = cal(1, 2)
        # print(calValue)
        # >> (3, -1, 2)   # tuple로 출력됨

        # 계산한 첫번째 결과값은 xx, 두번째 결과값은 yy, 세번째 결과값은 zz
            # print(f"계산한 첫번째 결과값은 {calValue[0]}, 두번째 결과값은 {calValue[1]}, 세번째 결과값은 {calValue[2]}")
            # >> 계산한 첫번째 결과값은 3, 두번째 결과값은 -1, 세번째 결과값은 2
# 2개의 숫자 input과 더하기/빼기/곱하기 input했을 때 원하는 값 출력
        # def cal(a, b, c):
        #     if c == 'plus':
        #         result = a + b
        #     elif c == 'minus':
        #         result = a - b
        #     elif c == 'multiply':
        #         result = a * b
        #     return result

        # 더하기한 값 출력
            # print(cal(1, 2, 'plus'))
        # 마이너스한 값 출력
            # print(cal(2, 1, 'minus'))
        # 곱하기한 값 출력
            # print(cal(2, 2, 'multiply'))
# 함수에서 default(초기값) 미리 세팅
        # def cal(a, b, c = 'plus'):          # c 옵션을 미리 세팅하면 c 값이 input 안됐을 때 default로 'plus'가 됨
        #         if c == 'plus':
        #             result = a + b
        #         elif c == 'minus':
        #             result = a - b
        #         elif c == 'multiply':
        #             result = a * b
        #         return result

        # print(cal(1, 2))
        # >> 3
    # 초기값(default)의 자리 순서를 꼭 맞춰야 할까?
        # 아니다. key value를 호출하는 것처럼 아래와 같이 하면 된다 (예) print(n, end = ' '))
# 매개변수의 순서를 안맞추고도 원하는 매개변수 자리에 값을 넣어 함수를 호출하는 방법
        # def whoAreYou(name, age, gender):
        #     print(f"제 이름은 {name}이고, 나이는 {age}, 성별은 {gender}입니다.")

        # whoAreYou(age=19, name='홍길동', gender='남자')
        # >> 제 이름은 홍길동이고, 나이는 19, 성별은 남자입니다.
    # python에서 default값 세팅하는 대표적인 예시: print()
        # print('hello')
        # print('world')
        # >> hello
        #    world
    # print 2개를 사용해서 줄바꿈 없이 hello world라고 출력
        # print('hello', end=' ')          # print()함수에 내제되어 있는 end = "\n"을 덮어씌우는 것임!
        # print('world')
        # >> hello world

# 지역변수, 전역변수
    # 지역변수: 함수 내에서의 변수, 함수 내에서만 유효, 함수 밖에서 인식불가
    # 전역변수 global variable: 함수 밖에서의 변수, 함수 내에서 인식가능

        # a = 100                     # 전역변수
        # def sum(a, b):                        # 여기서 a의 값은 10인가 100인가? -> 전역변수인 a=100보다 함수내에서 선언한 a=10가 우선적으로 인식된다
        #     result = a + b          # 지역변수
        #     return result           # 지역변수

        # result = sum(10, 20)        # 전역변수
        # print(result)                        
                                                # 함수내의 result라는 변수는 함수밖에서는 인식불가
                                                # result를 프린트할 수 있었던 것은, 함수내에서 어떤값을 return 해줬기 때문이다

    # for문마다 같은 변수를 사용하는 것은 전역변수이기는 하지만 재할당해서 사용하는 것이므로 어차피 reset돼서 문제되지 않는다
        # lista = [10, 20, 30]
        # for a in range(len(lista)):
        #     print(a)
        # for a in range(len(lista)):
        #     print(a)
        # print(a)
        # >>  0
        #     1
        #     2
        #     0
        #     1
        #     2
        #     2
    # 이중 for문을 사용할 떄에는 문제가 될 여지가 있다 - 다중 for문을 사용할 때에는 상위의 for문의 변수르 ㄹ잃어버리게 되므로, 다른 변수명 사용해야된다
        # 문제되는 예시:
            # lista = [10, 20, 30]
            # for a in range(len(lista)):
            #     for a in range(len(lista)):
            #         print(a)
        # 괜찮은 예시:
            # lista = [10, 20, 30]
            # for a in range(len(lista)):
            #     for b in range(len(lista)):
    # global: 함수 내에서 전역변수에 영향을 끼치는 방법
        # 기본적으로 함수 내에서 함수 밖의 전역변수를 수정할 수 없다 - 저장되는 메모리 위치가 다르기 때문이다

            # result = 0
            # def sum(a):
            #     global result
            #     result += a
            #     return result
            # value = sum(10)
            # print(value)
            # >> 10

    # 객체는 힙메모리 영역에 저장되는데, 함수 내에서도 접근하여 추가/수정이 가능
    # 스텍 영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지 않는다
            # lista = [2, 3, 4]
            # def appendTest(input1, input2):
            #     input1.append(input2)

            # appendTest(lista, 5)
            # print(lista)
            # >> [2, 3, 4, 5]

# 변수의 효력 범위 - pythontutor.com
    # 메모리구조
        # 데이터/메소드 영역 - 클래스, 전역 변수
        # 힙 영역 - 객체
        # 스택 영역 - 지역 변수, 매개 변수

# 만약 지역변수가 함수호출이 끝난 뒤에도 남아있다면 어떻게 출력될까?
        # def test1(result):
        #     result += 10
        #     return result
        # def test2(result):
        #     result += 100
        #     return result
        # a = test1(20)
        # print(a)
        # b = test2(20)
        # print(b)

# def mySort를 정의하고, 호출할 때 mySort(lista)한 다음에 print(lista)
        # a = 0
        # def mySort(lista):
        #     for a in range(len(lista)-1):
        #         # 두번째 for문은 비교의 대상이 되는 index를 의미
        #         for b in range(a+1, len(lista)):
        #             if lista[a] > lista[b]:
        #                 lista[a], lista[b] = lista[b], lista[a]
        #                 # 자리 change
        #                 # lista[a], lista[b] = lista[b], lista[a]
        # lst = [-5, 1, 1, 23, 6, 7, 8, 1]
        # mySort(lst)
        # print(lst)
        # >> [-5, 1, 1, 1, 6, 7, 8, 23]
# lista에 listb를 담으면, 객체의 메모리 주소가 복사가 된다
            # 그래서, listb가 lista와 동일한 (메모리) 주소, 동일한 데이터를 갖게 된다
        # lista = [5, 1, 2]
        # listb = lista
            # 주소를 출력하는 함수: id
        # print(id(lista))
        # print(id(listb))
        # >> 4300756096
        #    4300756096
            # 주소가 같으면 lista = listb이며 listb = lista인 것과 같다 - 이름만 다를 뿐 같은 메모리 주소를 갖고 있어서 둘 중 하나만 수정하더라도 다른 하나도 수정이 된다
            # lista와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy함수 사용
        # import copy
        # listb = copy.copy(lista)      
            # copy.copy(lista)는 얕은 복사 즉, 객체 안의 객체의 값은 메모리 주소로 복사가 된다.
            # 깊은 복사는 copy.deepcopy(lista)를 사용하여 객체의 객체도 모두 value로 복사한다.
        # listb = copy.deepcopy(lista)
        # print(id(lista))
        # print(id(listb))
        # print(listb)
        # >> 4300756096
        #    4343243648
        #    [5, 1, 2]

# immutable: int, string, tuple, bool
# mutable: list, dict, set