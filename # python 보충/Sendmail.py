import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendMail(from_addr, to_addr, subject, content, files=[]):
    # 컨텐츠형식 (plain or html)
    content_type ="plain"
    # 로그인계정이름 (네이버=아이디, 구글=메일주소)
    username ="w2crosss@gmail.com"
    # 비밀번호 (네이버=개인비밀번호,애플리케이션비밀번호, 구글=앱비밀번호)
    password ="kgir mquj laqj jwmm"
    # 구글 발송 서버 주소와 포트 (고정값)
    smtp ="smtp.gmail.com"
    port =587
    # 네이버 발송 서버 주소와 포트 (고정값)
    # #smtp = "smtp.naver.com"
    # #port = 465

    # 메일 발송정보를 저장하기 위한 객체
    msg = MIMEMultipart()

    msg['Subject']= subject  # 메일제목
    msg['From']= from_addr   # 보내는사람
    msg['To']= to_addr       # 받는사람

    # 본문 설정 -> 메일의 내용과 형식 지정
    msg.attach(MIMEText(content, content_type))

    # 리스트 변수의 원소가 하나라도 존재할 경우 True
    if files:
        for f in files:
            # 바이너리(b) 형식으로읽기(r)
            with open(f,'rb') as a_file:
                # 전체경로에서파일의이름만추출            
                basename = os.path.basename(f)
                # 파일의 내용과 파일 이름을 메일에 첨부할 형식으로 변환            
                part = MIMEApplication(a_file.read(), Name=basename)
                
                # 파일첨부            
                part['Content-Disposition']='attachment; filename="%s"'% basename            
                msg.attach(part)
    mail = SMTP(smtp)
    # 메일서버접속
    mail.ehlo()
    # 메일서버연동설정
    mail.starttls()
    # 메일서버로그인
    mail.login(username, password)
    # 메일보내기
    mail.sendmail(from_addr, to_addr, msg.as_string())
    # 메일서버접속종료
    mail.quit()

if __name__ == "__main__":
    sendMail ("w2crosss@gmail.com", "redlenz@naver.com", "제목입니다.", "내용입니다.")