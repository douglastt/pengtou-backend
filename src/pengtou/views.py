from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
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


@csrf_exempt
def activity(request):
    res = {"code": 0, "message":"成功"}
    if request.method == "GET":
        try:
            id = request.GET.get("id")
            a = models.Activity.objects.get(id=id)
            act_ser = serializer.ActivitySerializer(a)
            # user = serializers.serialize("json", u)
            json_rend = JSONRenderer()
            json_rend.encoder_class = serializer.PengtouJsonEncoder
            act_data = json_rend.render(act_ser.data)
            res["activity"] = json.loads(act_data)
            # print(user_data)
        except Exception as e:
            print("error:", e)
            res["code"] = 1
            res["message"] = "没有找到活动"
    elif request.method == "POST":
        try:
            id = request.GET.get("id")
            tag = request.GET.get("tag")
            address_final = request.GET.get("address_final")
            time_on = request.GET.get("time_on")
            time_up = request.GET.get("time_up")
            is_finish = request.GET.get("is_finish")
            # 如果post请求中带有id参数，则为更新操作，否则为增加用户操作
            if id == None:
                models.Activity.objects.create(tag=tag, address_final=address_final, time_on=time_on, time_up=time_up, is_finish=is_finish)
            else:
                u = models.Activity.objects.get(id=id)
                tag = u.tag if tag == None else tag
                address_final = u.address_final if address_final == None else address_final
                time_on = u.time_on if time_on == None else time_on
                time_up = u.time_up if time_up == None else time_up
                is_finish = u.is_finish if is_finish == None else is_finish
                models.Activity.objects.filter(id=id).update(tag=tag, address_final=address_final, time_on=time_on, time_up=time_up, is_finish=is_finish)
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "新增/更新活动失败"
    elif request.method == "DELETE":
        try:
            id = request.GET.get("id")
            print("delete method", request.GET.get("id"))
            models.Activity.objects.filter(id=id).delete()
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "删除活动失败"
    return JsonResponse(res)


@csrf_exempt
def user_activity(request):
    res = {"code": 0, "message":"成功"}
    if request.method == "GET":
        try:
            user_id = request.GET.get("user_id")
            activity_id = request.GET.get("activity_id")
            ua = models.UserActivity.objects.get(user_id=user_id, activity_id=activity_id)
            ua_ser = serializer.UserActivitySerializer(ua)
            # user = serializers.serialize("json", u)
            json_rend = JSONRenderer()
            json_rend.encoder_class = serializer.PengtouJsonEncoder
            act_data = json_rend.render(ua_ser.data)
            res["user_activity"] = json.loads(act_data)
            # print(user_data)
        except Exception as e:
            print("error:", e)
            res["code"] = 1
            res["message"] = "没有找到用户活动"
    elif request.method == "POST":
            user_id = request.GET.get("user_id")
            activity_id = request.GET.get("activity_id")
            address_start = request.GET.get("address_start")
            estimated_time = request.GET.get("estimated_time")
            voting_id = request.GET.get("voting_id")
            users = models.User.objects.filter(id=user_id)
            user = users[0] if users.count() > 0 else None
            if user == None:
                res["code"] = 1
                res["message"] = "没有找到用户"
                return JsonResponse(res)
            activities = models.Activity.objects.filter(id=activity_id)
            activity = activities[0] if activities.count() > 0 else None
            if activity == None:
                res["code"] = 1
                res["message"] = "没有找到活动"
                return JsonResponse(res)
            votings = models.Activity.objects.filter(id=voting_id)
            voting = votings[0] if votings.count() > 0 else None
            try:
                ua = models.UserActivity.objects.get(user=user, activity=activity)
                address_start = ua.address_start if address_start == None else address_start
                estimated_time = ua.estimated_time if estimated_time == None else estimated_time
                voting = ua.voting if voting == None else voting
                models.UserActivity.objects.filter(user=user, activity=activity).update(address_start=address_start, estimated_time=estimated_time,voting=voting)
            except Exception as e:
                print("cannot update:", e)
                # raise e
                try:
                    models.UserActivity.objects.create(user=user, activity=activity, address_start=address_start, estimated_time=estimated_time, voting=voting)
                except Exception as e:
                    print("exception is", e)
                    res["code"] = 1
                    res["message"] = "新增/更新用户活动失败"
    elif request.method == "DELETE":
        try:
            user_id = request.GET.get("user_id")
            activity_id = request.GET.get("activity_id")
            users = models.User.objects.filter(id=user_id)
            user = users[0] if users.count() > 0 else None
            if user == None:
                res["code"] = 1
                res["message"] = "没有找到用户"
                return JsonResponse(res)
            activities = models.Activity.objects.filter(id=activity_id)
            activity = activities[0] if activities.count() > 0 else None
            if activity == None:
                res["code"] = 1
                res["message"] = "没有找到活动"
            models.UserActivity.objects.filter(user=user, activity=activity).delete()
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "删除用户活动失败"
    return JsonResponse(res)


@csrf_exempt
def voting(request):
    res = {"code": 0, "message": "成功"}
    if request.method == "GET":
        try:
            id = request.GET.get("id")
            v = models.Voting.objects.get(id=id)
            vot_ser = serializer.VotingSerializer(v)
            # user = serializers.serialize("json", u)
            json_rend = JSONRenderer()
            json_rend.encoder_class = serializer.PengtouJsonEncoder
            vot_data = json_rend.render(vot_ser.data)
            res["voting"] = json.loads(vot_data)
            # print(user_data)
        except Exception as e:
            print("error:", e)
            res["code"] = 1
            res["message"] = "没有找到投票"
    elif request.method == "POST":
        id = request.GET.get("id")
        choose = request.GET.get("choose")
        num = request.GET.get("num")
        address_id = request.GET.get("address_id")
        addresses = models.PreferredLocation.objects.filter(id=address_id)
        address = addresses[0] if addresses.count() > 0 else None
        if address == None:
            res["code"] = 1
            res["message"] = "没有找到地址"
            return JsonResponse(res)
        try:
            # 如果post请求中带有id参数，则为更新操作，否则为增加用户操作
            if id == None:
                models.Voting.objects.create(choose=choose, num=num, address=address, created_at=timezone.now(), updated_at=timezone.now())
            else:
                v = models.Voting.objects.get(id=id)
                choose = v.choose if choose == None else choose
                num = v.num if num == None else num
                models.Voting.objects.filter(id=id).update(choose=choose, num=num, updated_at=timezone.now())
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "新增/更新投票失败"
    elif request.method == "DELETE":
        try:
            id = request.GET.get("id")
            # print("delete method", request.GET.get("id"))
            models.Voting.objects.filter(id=id).delete()
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "删除投票失败"
    return JsonResponse(res)


@csrf_exempt
def preferred_location(request):
    res = {"code": 0, "message": "成功"}
    if request.method == "GET":
        try:
            id = request.GET.get("id")
            l = models.PreferredLocation.objects.get(id=id)
            pl_ser = serializer.PreferredLocationSerializer(l)
            # user = serializers.serialize("json", u)
            json_rend = JSONRenderer()
            json_rend.encoder_class = serializer.PengtouJsonEncoder
            pl_data = json_rend.render(pl_ser.data)
            res["preferred_location"] = json.loads(pl_data)
            # print(user_data)
        except Exception as e:
            print("error:", e)
            res["code"] = 1
            res["message"] = "没有找到地址"
    elif request.method == "POST":
        id = request.GET.get("id")
        type = request.GET.get("type")
        name = request.GET.get("name")
        location = request.GET.get("location")
        score = request.GET.get("score")
        try:
            # 如果post请求中带有id参数，则为更新操作，否则为增加用户操作
            if id == None:
                models.PreferredLocation.objects.create(type=type, name=name, location=location, score=score)
            else:
                l = models.PreferredLocation.objects.get(id=id)
                type = l.type if type == None else type
                name = l.name if name == None else name
                location = l.location if location == None else location
                score = l.score if score == None else score
                models.PreferredLocation.objects.filter(id=id).update(type=type, name=name, location=location, score=score)
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "新增/更新地址失败"
    elif request.method == "DELETE":
        try:
            id = request.GET.get("id")
            # print("delete method", request.GET.get("id"))
            models.PreferredLocation.objects.filter(id=id).delete()
        except Exception as e:
            print("exception is", e)
            res["code"] = 1
            res["message"] = "删除地址失败"
    return JsonResponse(res)

