from rest_framework import serializers
from . import models
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = "__all__"


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserActivity
        fields = "__all__"


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Voting
        fields = "__all__"


class CommonProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommonProblem
        fields = "__all__"


class PreferredLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PreferredLocation
        fields = "__all__"


class PengtouJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            # print("encoding json using utf-8")
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
