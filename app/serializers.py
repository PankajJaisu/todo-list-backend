from rest_framework import serializers 
from .models import * 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        exclude = ['created_at']