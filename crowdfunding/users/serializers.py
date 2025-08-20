from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        # kwargs: keyword arguments
        # 'write_only': 

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    # **: related to kwargs
    # purpose of defining the function of create: to protect password