from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        # kwargs: keyword arguments
        # 'write_only': security and design feature that controls how password is handled in serializers
        # write_only: accept input, never output; "read_only": accept output, never input
    

    def create(self, validated_data):
     # purpose of defining the function of create: to protect password
        return CustomUser.objects.create_user(**validated_data)
    # create_user() automatically hashes passwords
    # "**" operator: related to kwargs, unpack the dictionary into keyword arguments