from rest_framework import serializers
from . import models
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class PengtouJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            print("encoding json using utf-8")
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
