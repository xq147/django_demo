# urls
from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'user'
urlpatterns = [
    # 在在 urls.py 中配置中配置跨域访问
    # path('user/register/', csrf_exempt(views.register), name='register'),
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login, name='login'),

]
