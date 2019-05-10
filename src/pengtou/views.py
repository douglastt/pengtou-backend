from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from . import models
# @csrf_exempt
# @method_decorator(csrf_exempt, name="user")
# class UserView(View):
#     def get(self, request, id):
#         u = models.User.objects.get(id=id)
#         if u == None:
#             print("no user found")
#         else:
#             print(u)
#     def post(self, request):
#         res = {"code": 0, "message": "成功"}
#         nickname = request.POST.get("nickname")
#         avatar_url = request.POST.get("avatar_url")
#         gender = request.POST.get("gender")
#         province = request.POST.get("province")
#         city = request.POST.get("city")
#         language = request.POST.get("language")
#         # nickname = request.POST.get("nickname")
#
#
#         print(nickname, avatar_url, gender)
#         try:
#             # u = models.User()
#             # nickname = request.POST.get("nickname")
#             models.User.objects.create(nickname=nickname, avatar_url=avatar_url, gender=1, province=province, city=city,
#                                        language=language)
#         except Exception as e:
#             print(e)
#             res["code"] = 1
#             res["message"] = "新增用户失败"
#         return JsonResponse(res)
@csrf_exempt
def user(request):
    res = {"code": 0, "message":"成功"}
    if request.method == "GET":
        try:
            u = models.User.objects.get(id=id)
            print(u)

        except Exception:
            print("no user found")
            res["code"] = 1
            res["message"] = "没有找到用户"
    elif request.method == "POST":
        try:
            # u = models.User()
            # nickname = request.POST.get("nickname")
            # id = 1, nickname = "", avatar_url = "", province = "", city = "", language = ""
            args = QueryDict(request.body)
            nickname = request.GET.get("nickname")
            avatar_url = request.GET.get("avatar_url")
            gender = request.GET.get("gender")
            province = request.GET.get("province")
            city = request.GET.get("city")
            language = request.GET.get("language")

            models.User.objects.create(nickname=nickname, avatar_url=avatar_url, gender=1, province=province, city=city, language=language)
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "新增用户失败"
    return JsonResponse(res)

# def user(request, id, nickname, avatar_url, province, city, language):


def test(request):
    return HttpResponse("hello response")

def testJson(request):
    testmap = {"status": 0, "data": "hello data"}
    return JsonResponse(testmap)