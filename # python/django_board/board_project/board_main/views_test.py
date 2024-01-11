from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test

# Create your views here.

# get 요청시 html 파일 그대로 return
def test_html(request):
    # render(): 웹개발에서 일반적으로 화면을 return 해줄 때 사용하는 용어
    return render(request, 'test/test.html')         # django에서 알아서 template이라는 폴더 안의 파일을 찾는다 (약속되어있음)

# get 요청시 html + data return         # 단일 data 넣어올 때
def test_html_data(request):
    my_name = "hongildong"
    return render(request, 'test/test.html', {'name': my_name})

# get 요청시 html + multi data return
def test_html_multi_data(request):
    data = {
        'name': 'hongildong',
        'age': 20
    }
    return render(request, 'test/test.html', {'data': data})

# get 요청시 data만 return
def test_json_data(request):
    data = {
        'name': 'hongildong',
        'age': 20
    }
    # JsonResponse(): python의 dict와 유사한 json의 형태로 변환해서 return
    return JsonResponse(data)

# 사용자가 get 요청으로 데이터를 넣어올 때            -> 사용자가 url주소에 데이터를 입력해야 됨
# 사용자가 get 요청으로 데이터를 넣어오는 2가지 방식:
    # 1. 쿼리 파라미터 방식: 
        # localhost:8000/author?id=10
            # localhost:8000/author 까지 url
            # ? 후에 데이터 입력
            # 여러가지 값은 사이에 & 로 구분
        # localhost:8000/author?id=10&name=hongildong
            # 여러가지 데이터를 넣고 싶은 경우 & 사용
    # 2. path variable 방식 (좀 더 현대적인 방식):
        # localhost:8000/author/10
            # localhost:8000/author 까지 url
            # / 후에 데이터 값 입력
def test_html_parameter_data(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    print(id)
    print(name)
    return render(request, 'test/test.html', {}) 


# 사용자가 get요청으로 넘긴 data를 화면에 dict 형태로 던져주고
# 화면에는 이름은 - 이메일은 - 비밀번호는 - 로 띄워줄 때       
# -> 사용자가 url주소에 데이터를 입력해야 됨: http://localhost:8000/silsup_data?name=%EC%95%88%EB%8B%A4%EC%9C%A4&email=dayoonz@naver.com&password=1234
def test_html_silsup_data(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    data = {
        'name': name,
        'email': email,
        'password': password
    }
    return render(request, 'test/test.html', {'data': data}) 

# 사용자가 get 요청으로 데이터를 넣어올 때            
# -> 사용자가 url주소에 데이터를 입력해야 됨: http://localhost:8000/silsup_data2/10
def test_html_silsup_data2(request, my_id):
    print(my_id)
    return render(request, 'test/test.html', {}) 
# terminal에 10 이라고 출력됨



# form 태그를 활용한 post 방식:

# 화면을 rendering 해주는 method
# test/test_post_form.html 만들고 form 태그로 name, email, password
# def test_post_form(): 에서 return test/test_post_form.html + url 매핑
def test_post_form(request):
    return render(request, 'test/test_post_form.html') 

# def test_post_handle(request):
#     name = request.POST['my_name']
#     email = request.POST['my_email']
#     password = request.POST['my_password']
#     print(name)
#     print(email)
#     print(password)
#     return HttpResponse('ok')

def test_post_handle(request):
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        # DB에 insert -> save() 함수 사용
        # DB의 테이블과 sync가 맞는 test클래스에서 객체를 만들어 save
        t1= Test()
        t1.name = my_name
        t1.email = my_email
        t1.password = my_password
        t1.save()
        return redirect('/') # -> '' 안에 /를 넣으면 home으로 가게 된다, 즉, localhost:8000/ 로 redirect 하게 됨
    else: 
        return render(request, 'test/test_post_form.html')
    
def test_select_one(request, my_id):
    # 단건만을 조회할 땐 get 함수
    t1 = Test.objects.get(id=my_id)
    return render(request, 'test/test_select_one.html', {'data':t1})
    # -> url에 http://localhost:8000/test_select_one/id값 입력
    # -> 예) http://localhost:8000/test_select_one/3

# def test_select_all(request):
#     # 모든 data 조회시 select * from xxxx; all()함수 사용
#     # dicta.keys()
#     # for문으로 print
#     tests = Test.objects.all()
#     print(type(tests))
#     for a in tests:
#         print(a.name) 
#         # tests는 dict가 아니라 객체(object)이기 때문에 a.'name'이 아니라 a.name과 같이 print에 넣는다
#         print(a.email)
#         print(a.password)
#     return render(request, 'test/test_select_all.html')

def test_select_all(request):
    # 모든 data 조회시 select * from xxxx; all()함수 사용
    # dicta.keys()
    # for문으로 print
    tests = Test.objects.all()
    return render(request, 'test/test_select_all.html', {"datas": tests})

# where조건으로 다건을 조회할 땐 filter()함수 사용
# Test.objects.filter(name = my_name) -> 다건 가정
# filter()
def test_filter(request):
    # localhost:8000/test_filter?name=pearl
    my_name = request.GET.get('name')
    tests = Test.objects.filter(name = my_name)
    return render(request, 'test/test_filter.html', {"datas": tests}) 

# update를 하기 위해서는 해당건을 사전에 조회하기 위한 id값이 필요
# method는 등록과 동일하게 save()함수 사용
# save() 함수는 신규객체를 save하면 insert, 기존 객체를 save하면 update
def test_update(request):
    if request.method == 'POST':
        my_id = request.POST['my_id']
        t1 = Test.objects.get(id=my_id)
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        t1.name = my_name
        t1.email = my_email
        t1.password = my_password
        t1.save()
        # 삭제는 delete()함수 사용. update와 마찬가지로 기존객체 조회 후 delete()
        # t1.delete()를 하면 삭제
        return redirect('/')
    else: 
        return render(request, 'test/test_update.html')