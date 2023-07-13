# # open: file 시스템 입출력 라이브러리
#     # mode(w, r, a)을 갖고 있다
#         # w: write(덮어쓰기), r:read. a:추가
#     # open을 했을 떄 해당 파일명이 없으면 자동생성한다.




# # f = open("test.txt", "w")
# # f.close()




# # w mode

# f = open("test.txt", "w", encoding="UTF-8")       # encoding="UTF-8" 은 텍스트 파일에서 한글이 안 깨지게 해준다
# for i in range(10):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()



# # r mode

# f = open("test.txt", "r", encoding="UTF-8") 
# line = f.readline()                                           # f.readline() - 첫번째 줄만 가져오는 함수
# print(line)
# f.close

# with ... as f: 은 나중에 안 닫아도 된다(f.close 필요 없)

# with open("test.txt", "r", encoding = "utf-8") as f:
    # f.write(Hello World\n")
    # f.write(Hello World\n")
    # f.write(Hello World\n")
    # f.write(Hello World\n")





# while, if문, readline으로 전체 출력
    # 방법 1
        # f = open("test.txt", "r", encoding="UTF-8") 
        # line = f.readline
        # while line:                     
        #     print(line)
        #     line = f.readline()    
        # f.close
    # 방법 2
        # f = open("test.txt", "r", encoding="UTF-8") 
        # while True: 
        #     line = f.readline()
        #     print(line)
        #     if not line:
        #         break
        # f.close

        # f = open("test.txt", "r", encoding="UTF-8") 
        # lines = f.readlines()                                 # f.readlines() - 데이터를 리스트형태로 라인별로 담아준다
        # print(lines)
        # >> ['0번째 줄입니다.\n', '1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n']

        # f = open("test.txt", "r", encoding="UTF-8") 
        # lines = f.read()                                      # f.read() - 데이터를 한꺼번에 문자열 형태로 담아준다
        # print(lines)
        # >> 0번째 줄입니다.
        #    1번째 줄입니다.
        #    2번째 줄입니다.
        #    3번째 줄입니다.
        #    4번째 줄입니다.
        #    5번째 줄입니다.
        #    6번째 줄입니다.
        #    7번째 줄입니다.
        #    8번째 줄입니다.
        #    9번째 줄입니다.




# # a mode

# # a옵션으로 추가모드 - 0-9번째 줄입니다. --> 10-19번째 줄입니다.

# f = open("test.txt", "a", encoding="UTF-8")
# for i in range(10, 20):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()



# # 파이썬에서 객체를 생성하고 나면 힙메모리에 객체가 할당된다.
# # 객체의 사용이 끝나면 객체를 close 해줘야 하나?
# # 그럴 필요 없다. 왜냐하면 파이썬에는 GC(Garbage Collector)가 내장되어 있어서 자동으로 사용빈도가 낮은 데이터는 메모리에서 삭제를 해준다.
# # 그러나 파일시스템은 그렇지 못하므로 직접 닫아줘야 된다. 그래야 메모리 낭비가 없다.







# # os 라이브러리를 활용한 디렉터리 내에 파일 검색
# import os



# # .py로 끝나는 파이썬확장파일을 search

# searchDir = '/Users/dayoonz/Desktop/안다윤'           # 어느 디렉토리에서 search할지 선언
# dirList = os.listdir(searchDir)                     # 디엑토리 안에 있는 폴더랑 파일 목록을 뽑아내기 # os.listdir()
# for dir in dirList:
#     dirTuple = os.path.splitext(dir)                # 파일/폴더 이름을 tuple 형태로 split # os.path.splitest() >> (파일/폴더명, .py)
#     if(dirTuple[1] == '.py'):
#         fullPath = os.path.join(searchDir, dir)
#         print(fullPath)



# # 그 다음 폴더까지 검색 - 이중 for 문 사용

# searchDir = '/Users/dayoonz/Desktop/안다윤'
# dirList = os.listdir(searchDir)
# for dir in dirList:
#     filename = os.path.join(searchDir, dir)
#     if os.path.isdir(filename):
#         dirList2 = os.listdir(filename)
#         for dir2 in dirList2:
#             dirTuple2 = os.path.splitext(dir2)
#             if(dirTuple2[1] == '.py'):
#                 fullPath = os.path.join(filename, dir2)
#                 print(fullPath)
#     dirTuple = os.path.splitext(dir)
#     if(dirTuple[1] == '.py'):
#         fullPath = os.path.join(searchDir, dir)
#         print(fullPath)



# # 모든 폴더 검색 -> 재귀 함수 사용

# def searchRecur(searchDir):
#     try:                                                            # 파일명을 찾는 데에는 예외가 있을 경우가 많아서 try except 걸어주기
#         dirList = os.listdir(searchDir)
#         if not dirList:                                             # 디렉토리 안에 파일이나 폴더가 더 이상 없을 때 종료시키기
#             return
#         for dir in dirList:
#             filename = os.path.join(searchDir, dir)
#             if os.path.isdir(filename):                             # return true if the pathname refers to an existing directory
#                 searchRecur(filename)                               # 반복되는 구간에다가 재귀함수 사용 - searchRecur()
#             dirTuple = os.path.splitext(dir)
#             if(dirTuple[1] == '.py'):
#                 fullPath = os.path.join(searchDir, dir)
#                 print(fullPath)
#     except Exception:
#         print("예외입니다.")
# searchDir = '/Users/dayoonz/Desktop/안다윤'
# searchRecur(searchDir)







# 개인 연습
# tips.csv의 정보를 갖고 tips_copy.csv를 만들어서 tips_percentage정도 추가하기
    # fr= open("tips.csv", "r", encoding="UTF-8")
    # lines = fr.readlines()                                 # f.readlines() - 데이터를 리스트형태로 라인별로 담아준다
    # fr.close()

    # rw= open("tips_copy.csv", "w", encoding="UTF-8")
    # lista = []
    # listb = []
    # rw.write(lines[0])
    # for a in range(1, 245):
    #     lista.append(lines[a])
    # for b in lista:
    #     listb.append(b.split(','))
    # for a in listb:
    #     a[-1] = a[-1].replace('\n','')
    #     tips_percentage = round((float(a[1])/float(a[0])*100), 1)
    #     a.append(str(tips_percentage)+"%\n")
    #     a = ','.join(a)
    #     rw.write(a)
    # rw.close()

