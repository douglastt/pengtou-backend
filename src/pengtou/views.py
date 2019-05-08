from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def test(request):
    return HttpResponse("hello response")

def testJson(request):
    testmap = {"status": 0, "data": "hello data"}
    return JsonResponse(testmap)