
# import하고 싶은 모듈이 있으면 import구문을 사용

# 기본 구조
    # import 패키지명.파일명
        # import module_test.module_statements
    # from 패키지명 import 파일명
        # from module_test import 13_module)statements
# 약어
    # as
    # 예) import 패키지명.파일명 as 약어
        # import module_test.module_statements as ms
        # print(ms.plus(10, 20))
# 예)
    # import module_test.module_statements as ms
    # print(ms.multiply(20, 10))
    # >> 200

import class_statements
c1 = class_statements.CalculatorChild()

# module명 만들 때 폴더의 모듈명은 숫자로 시작 가능하나 module을 import할 때에는 module명이 숫자로 시작할 수 없다

c1.plus(100)
print(f"modul_import의 result: {c1.result}")

