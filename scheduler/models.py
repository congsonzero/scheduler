from django.db import models


class Scheduler(models.Model):
    schedulerID = models.AutoField(primary_key=True)
    alarm = models.DateTimeField(blank=False,default="")
    # Time = models.IntegerField(blank=False,default="")

