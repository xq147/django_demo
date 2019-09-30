from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import uuid
import json
from .models import User, Question


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, uuid.UUID):
            return ''.join(str(obj).split('-'))
        else:
            return json.JSONEncoder.default(self, obj)


# @csrf_exempt 注解来标识一个视图可以被跨域访问
@csrf_exempt
def register(request):
    register_user = json.loads(request.body)
    username = register_user['username']
    password = register_user['password']
    user = User(username=username, password=password)
    user.save()
    if user.id:
        data = {'flag': 0, 'id': user.id}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def login(request):
    login_user = json.loads(request.body)
    username = login_user['username']
    password = login_user['password']
    user = get_object_or_404(User, username=username)
    out_user = user.user_vo()
    if user.password == password:
        data = {'flag': 0, 'user': out_user}
    else:
        data = {'flag': 1, 'msg': '用户名或密码错误！'}
    return HttpResponse(json.dumps(data), content_type='application/json')
