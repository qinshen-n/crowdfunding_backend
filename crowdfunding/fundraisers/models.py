from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers', # this provides a convenient reverse lookup name to access all the fundraisers created by a user by calling user.owned_fundraisers.all()
        on_delete=models.CASCADE # if users are deleted, all their associated fundraisers would be deleted 
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True, null=True)
    date_made = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser', 
        related_name='pledges',
        on_delete=models.CASCADE    
    )
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges',
        on_delete=models.CASCADE # if users are deleted, all their associated pledges would be deleted
    )