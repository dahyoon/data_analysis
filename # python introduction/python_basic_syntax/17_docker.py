# docker

# docker는 컨테이너 기반이며 경량화된 가상화 서버라고 생각하면 된다
# 가상화된 서버인 VM과 비교 (VM != docker) - VM보다 앞도적으로 속도 빠름, 가벼움
# 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼

# 리눅스 배포판
    # 리눅스란 unix를 기반으로 만들어진 무료 운영체제 커널
    # 리눅스에는 수백개의 배포판이 존재
    # 크게는 redhat계열, debain계열이 존재
    # docker에서 

# docker 이미지
# docker는 이미지 기반으로 동작
# 이미지란 컨테이너를 실행하기 위한 압축파일과 같은 개념
# 하나의 이미지는 여러 컨테이너를 생성할 수 있고, 컨테이너가 삭제되더라도 이미지는 변하지 않는다
    # docker images, docker ps 테스트

# 컴표터 세팅
# 1) docker 다운로드
# 2) docker 가상화를 위한 세팅 (공유해준 명령어)
# 3) terminal 에다가 아래 실행문 입력:
    # 1. docker run -it ubuntu (우분투 이미지 다운로드 및 실행)
    # 2. ctrl + c 또는 exit
    # 3. docker ps -a 

# docker 명령어
    # docker stop 컨테이너ID
    # docker images 
        # docker 이미지 목록을 조회하는 명령어)
    # docker run -it --name my_ubuntu ubuntu 
        # 이름을 지정해서 우분투 리눅스 프로세스 생성; 우분투 실행시
    # docker start 컨테이너ID 
        # 우분투는 최초 생성 후 exit하게 되면 다시 start시켜줘야 된다
    # docker rmi 이미지ID
    # docker ps
        # 실행중인 프로세스만 출력
    # docker ps -a:
        # 모든 프로세스 출력 (실행 중 & 실행 안하고 있는 것들도)
    # docker start 컨테이너ID
        # 꺼져 있는 프로세스를 실행 시켜줌

# dockers 프로세스 삭제 (remove)
    # 1) docker stop 컨테이너ID
    # 2) docker rm 컨테이너ID

# docker 컨테이너 내부로 접속
    # docker exec -it 컨테이너명 /bin/bash



# docker 접속!
    # 1) docker ps -a
    # 2) docker exec -it 컨테이너명 /bin/bash


# makemigrations 와 migrate
    # python3 manage.py makemigrations --> DDL문 생성
    # python3 manage.py migrate --> DDL문 생성 후 반영   




# 리눅스 명령어

# 디렉토리 이동
    # cd 이동할 위치
# 현재 위치 조회 명령어
    # pwd
# ls 명령어 (파일/디렉토리 목록 조회 명령어)
    # ls
    # ls -a          # 숨긴 파일까지 조회
    # ls -al         # 정보까지 조회
    # ls -al 파일명    # 파일명 만 조회
    # ls -al test*   # test로 시작하는파일/폴더 조회 
# cd 명령어
    # 상대경로 (상위 폴더로 올라감)
        # cd ..                                 
    # 절대경로 이동 (가고자하는 폴더로 이동)
        # cd /가고자하는폴더
    # 홈 경로로 이동
        # cd
    # root경로로 이동
        # cd /

# .은 현재경로를 의미
# ..은 상위경로를 의미

# 최상단 root 경로는 / 로 표현
    # 이름 앞에 붙는 / 와 뒤에 오는 /의 의미는 완전 다르다
    # 이름 앞에 /를 붙이는 경우 root를 가리킨다
    # 이름 뒤에 오는 /는 저절로 붙는 것
# root계정은 모든 계정이 있는 super계정   

# 명령어 정리
    # clear - 입력중인 명령창 깨끗하게 정리
# 생성 명령어
    # 디렉토리 생성 명령어
        # mkdir 폴더명
    # 파일 생성 (빈 파일)
        # touch 파일명
# 삭제 명령어
    # rm -r 디렉토리명
    # rm -r 파일명
    # rm -r 삭제대상1 삭제대상2
    # rmi 이미지명
# 실행 중 명령어 취소
    # ctrl + c

# history 조회
    # 사용했던 명령어의 history

# 복사 후 붙여넣기
    # cp 복사대상 복사할곳과파일명
    # cp -r 하면 디렉토리까지 복사
# 이동/파일명 변경 명령어 (파일/디렉토리) - 잘라내서 붙여넣기
    # mv 이동대상 이동할곳과파일명              # 파일명은 바꾸고 싶으면 넣어도 되고 그대로 하고 싶으면 안 넣어도 됨
    # mv 원래파일/폴더명 바꿀파일/폴더명         # 더 정확하게 위치를 명시하고 싶으면 : mv 원래파일명 ./바꿀파일명

# cd /etc 해서 /etc로 이동
# cd my_folder 해서 my_folder로 이동
# 현재폴더 위치 출력(pwd)



# 기본 명령어 (실무에서 많이 사용)

# cat 파일명
    # text로 작성된 파일을 터미널화면에 출력
# more 파일명 
    # 텍스트로 작성된 파일을 페이지 단위로 출력
    # space를 통해 아래 페이지로 넘어감
# sudo 
    # 현재 계정에서 root계정의 권한을 빌려 명령어를 실행하는 것
    # 현재 사용자의 비번 입력
    # sudo adduser new_username

# apt : 리눅스 패키지 tool
    # apt-get update: 패키지 최신화하는 명령어
    # apt-get install vim: vi편집기 install하는 명령어

# vi 편집기
    # .txt 편집
        # vi test.txt 한 다음 enter 
        # i 누르면(타자) insert모드로 됨                        # i는 insert모드; x는 삭제모드; a ...
        # 원하는 글(hello world)을 쓰고 esc 누름                # esc는 명령모드 상태로 감
        # : 쓰고 wq(저장)) 쓰고 enter                         # :wq 는 저장; :q! 는 저장하지 않음
        # 밖으로 나와 있을 것임
        # cat test.txt 누르면 hello world가 출력 될 것임
    # .py 편집
        # vi test.py 한 다음 enter 
        # 위와 똑같음
# 입력모드
    # i 현재 커서부터 입력
    # a
    # o
    # x 단어 삭제
    # dd 행 삭제
    # gg 맨 위로 감
    # G 맨 아래로 감
    # $ 문장의 끝으로 이동
    # e 단어의 끝으로 이동
    # 숫자 0 해당라인에서 첫번째 단어로 이동
    # yy 복사 
    # p 붙여넣기
    # ctrl + f 다음 페이지이동
    # ctrl + b 이전 페이지 이동
    # q 저장 없이 종료, q! 저장 없이 강제종료
    # wq 저장 후 종료, wq! 저장 후 강제종료
# 명령모드
    # esc


# python 실행
    # python3 test.py 하여 test.py를 터미널에 실행시킴


# 사용자와 그룹관리
    # chmod nnn test.txt
        # 파일/디렉토리에 대해 소유자:소유그룹:그외(other)에 대한 권한설정
        # 권한의 구성
            # 권한은 3개의 part로 구성: owner, ownerGroup, other(그외))
            # 각 파트는 rwx(421) 권한으로로 구성 (read, write, 실행)
            # r:숫자4; w:숫자2 x:숫자1
        # 예) chmod 777 test.txt
            # test.txt파일의 소유자, 그룹, other에게 rwxrwxrwx권한을 부여한다는 의미
            # r:숫자4; w:숫자2 x:숫자1
            # chmod 777 test.txt --> 소유자, 소유자그룹, others 모두 읽고, 쓰고, 실행할 수 있음
            # chmod 644 test.txt --> 소유자는 읽고 쓸 수 있고, 소유자그룹과 other는 쓰기만 할 수 있음

        # ls -al 했을 때, 
            # 첫 컬럼 (예) drwxr-xr-x): 권한
                # 첫 문자 (예)d)는 파일/폴더 종류
                # 그 다음 3 문자씩 총 9개 문자는 권한 종류를 의미
                # 3세트 중 첫 세트는 소유자의 권한, 두번때 세트는 소유자그룹의 권한, 세번째 세트는 그 외의 권한
            # 3-4번째 컬럼 (예) root root): 소유자, 소유자그룹
            # 5번째 컬럼 (예) 4096): 용량
            # 6-8 컬럼 (예) Jun  2 00:48): utc 시간대

    # chown 소유자:소유그룹파일명
        # 해당 파일/디렉토리의 소유자와 소유자그룹을 새롭게 부여하는 명령어
    # 소유자와 소유자그룹
        # 소유자그룹: 특정한 사용자 list를 그룹으로 묶어놓은 개념. 리눅스에서 모든 사용자는 어떠한 소유자그룹에 소속돼있다.
# 디스크
    # df -h 
# 메모리
    # free 
    # free -h 
# CPU
    # top 
    # htop

# 파일검색
    # grep 
        # 특정 문자열을 찾을 때 사용
    # find
        # 특정 directory에서 특정 파일을 찾을 떄 사용
