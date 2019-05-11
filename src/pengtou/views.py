from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from . import serializer
import json
from . import models

@csrf_exempt
def user(request):
    res = {"code": 0, "message":"成功"}
    if request.method == "GET":
        try:
            id = request.GET.get("id")
            u = models.User.objects.get(id=id)
            user_ser = serializer.UserSerializer(u)
            # user = serializers.serialize("json", u)
            json_rend = JSONRenderer()
            json_rend.encoder_class = serializer.PengtouJsonEncoder
            user_data = json_rend.render(user_ser.data)
            res["user"] = json.loads(user_data)
            # print(user_data)
        except Exception as e:
            print("error:", e)
            res["code"] = 1
            res["message"] = "没有找到用户"
    elif request.method == "POST":
        try:
            id = request.GET.get("id")
            nickname = request.GET.get("nickname")
            avatar_url = request.GET.get("avatar_url")
            gender = request.GET.get("gender")
            province = request.GET.get("province")
            city = request.GET.get("city")
            language = request.GET.get("language")
            # 如果post请求中带有id参数，则为更新操作，否则为增加用户操作
            if id == None:
                models.User.objects.create(nickname=nickname, avatar_url=avatar_url, gender=gender, province=province, city=city, language=language)
            else:
                u = models.User.objects.get(id=id)
                nickname = u.nickname if nickname == None else nickname
                avatar_url = u.avatar_url if avatar_url == None else avatar_url
                gender = u.gender if gender == None else gender
                province = u.province if province == None else province
                city = u.city if city == None else city
                language = u.language if language == None else language
                models.User.objects.filter(id=id).update(nickname=nickname, avatar_url=avatar_url, gender=gender, province=province, city=city, language=language)
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "新增/更新用户失败"
    elif request.method == "DELETE":
        try:
            id = request.GET.get("id")
            print("delete method", request.GET.get("id"))
            models.User.objects.filter(id=id).delete()
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "删除用户失败"
    return JsonResponse(res)