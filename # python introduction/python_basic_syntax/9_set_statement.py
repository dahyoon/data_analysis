# set은 (수학)집합이라고도 함
# {} 사용
# type은 set
# s1 = {'이름', '나이', '성별'}
# index와 중복이 없음 (dictionary같이)
    #index로 접근 불가

# set 형변환 - list의 중복을 제거하기 위해 list를 set으로 형변환 시키는 방식 많이 사용
    # set(list) 아니면 set(str)
        # l1 = ['이름', '이름', '나이', '성별']
        # s1 = set(l1)  # s1 = set(['이름', '이름', '나이', '성별'])와 같음
        # print(s1)
        # >> {'나이', '성별', '이름'}   # 순서는 랜덤으로 출력됨
        # str1 = 'test'
        # s2 = set(str1)
        # print(s2)
        # >> {'t', 's', 'e'}
# set 개수 구하기
    # len(set)
        # s1 = {'나이', '성별', '이름'}
        # len(s1)
        # >> 3
# set 값 출력
    # index 불가!
    # for문 사용
        # s1 = {'이름', '나이', '성별'}
        # for a in s1:
            # print(a)
            # >> 이름
            #    성별
            #    나이
# 합집합
    # | - or(또는))
        # s1 = set([1, 2, 3, 4])
        # s2 = set([5, 6, 7, 8])
        # s3 = s1 | s2
        # print(s3)
        # >> {1, 2, 3, 4, 5, 6, 7, 8}
    # s1.union(s2)
        # s1 = set([1, 2, 3, 4])
        # s2 = set([5, 6, 7, 8])
        # s3 = s1.union(s2)
        # print(s3)
        # >> {1, 2, 3, 4, 5, 6, 7, 8}
# 교집합
    # &
        # s1 = set([1, 2, 3, 4, 5, 6])
        # s2 = set([5, 6, 7, 8])
        # s3 = s1 & s2
        # print(s3)
        # >> {5, 6}
    # s1.intersection(s2)
        # s1 = set([1, 2, 3, 4, 5, 6])
        # s2 = set([5, 6, 7, 8])
        # s3 = s1.intersection(s2)
        # print(s3)
        # >> {5, 6}
# 차집합
    # -
        # s1 = {1, 2, 3, 4, 5, 6}
        # s2 = {5, 6, 7, 8}
        # s3 = s1 - s2
        # print(s3)
        # >> {1, 2, 3, 4}
    # difference
        # s1 = {1, 2, 3, 4, 5, 6}
        # s2 = {5, 6, 7, 8}
        # s3 = s1.difference(s2)
        # print(s3)
        # >> {1, 2, 3, 4}
# 값 추가
    # set.add(값) - 한 값
        # s1 = {1, 2, 3, 4}
        # s1.add(5)
        # print(s1)
        # >> {1, 2, 3, 4, 5}
    # set.update(setnew) - 여러 값 추가(딕셔너리와 동일)
        # s1 = {1, 2, 3, 4}
        # s2 = {'a', 'b', 1}
        # s1.update(s2)
        # print(s1)
        # >> {'a', 1, 2, 3, 4, 'b'}
# 값 삭제
    # set.remove(값) - 없는 값을 지우려고 할 때 error 남
        # s1 = {1, 2, 3, 4}
        # s1.remove(1)
        # print(s1)
        # >> {2, 3, 4}
    # set.discard(값) - 없는 값을 지우려고 해도 error 안남 - 예외처리를 알아서 해줌 - 이걸 사용하는 것이 더 좋음!
        # s1 = {1, 2, 3, 4}
        # s1.discard(0)
        # print(s1)
        # >> {1, 2, 3, 4}
