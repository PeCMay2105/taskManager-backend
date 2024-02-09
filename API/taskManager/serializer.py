from .models import Task
from rest_framework import serializers


class taskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250)
    completed = serializers.BooleanField(default=False)

    def create(self,validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, outside_data):
        instance.title = outside_data.get('title', instance.title)
        instance.completed = outside_data.get('completed', instance.completed)
        instance.save()
        return instance
 