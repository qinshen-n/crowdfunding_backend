from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        # tell which model to covert and which fields it should include from the model
        model = apps.get_model('fundraisers.Fundraiser') 
        # include all fields
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.date_made = validated_data.get('date_made', instance.date_made)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        # Note: We do not allow the fundraiser or supporter to be changed via an update
        instance.save()
        return instance

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title) # if 'title' does not exist in this dictionary, it would return the current value of instance
        instance.description = validated_data.get('description', instance.description)
        instance.goal_amount = validated_data.get('goal_amount', instance.goal_amount)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('start_date', instance.end_date)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance