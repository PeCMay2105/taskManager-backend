from .models import Task
from rest_framework import serializers


class taskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250)
    completed = serializers.BooleanField(default=False)

    def create(self,validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self,outside_data):
        return Task.objects.update(**outside_data)
