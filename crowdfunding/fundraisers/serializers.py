from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        # tell which model to covert and which fields it should include from the model
        model = apps.get_model('fundraisers.Fundraiser') 
        # include all fields
        fields = '__all__'