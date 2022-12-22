from django.db import models

# Create your models here.
class Result(models.Model):
    hero = models.CharField(max_length=50, default="")
    heroID = models.IntegerField(default=0)
    item = models.CharField(max_length=50, default="")
    itemID = models.IntegerField(default=0)
    winrate = models.CharField(max_length=50, default="")
    usage = models.CharField(max_length=50, default="")
    queryTime = models.CharField(max_length=50, default="")
    totalMatches = models.IntegerField(default=0)