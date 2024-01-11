from django.urls import path
from . import views

urlpatterns = [
    # # path('url에 "http://localhost:8000/" 뒤에 입력할 주소명', views_test.views_test에서 쓸 함수명)
    # path('', views_test.test_html_data),
    # path('test_json', views_test.test_json_data),
    # path('multi_data', views_test.test_html_multi_data),
    # path('parameter_data', views_test.test_html_parameter_data),
    # path('silsup_data', views_test.test_html_silsup_data),
    # # localhost:8000/silsup_data?name=hong&email=hong@naver.com&password=1234
    # path('silsup_data2/<int:my_id>', views_test.test_html_silsup_data2),
    # # localhost:8000/silsup_data2/10
    # path('test_post_handle', views_test.test_post_handle),
    # path('test_select_one/<int:my_id>', views_test.test_select_one),
    # path('test_select_all', views_test.test_select_all),
    # path('test_filter', views_test.test_filter),
    # path('test_update', views_test.test_update)

    path('', views.home),
    path('authors/', views.author_list),
    path('author/new', views.author_new),
    path('author/<int:my_id>', views.author_detail),
    path('author/<int:my_id>/update', views.author_update),
    path('posts/', views.post_list),
    path('post/new', views.post_new),
    path('post/<int:my_id>', views.post_detail),
    path('post/<int:my_id>/update', views.post_update),

]

# localhost:8000/silsup_data?name=hong&email=hong@naver.com&password=1234