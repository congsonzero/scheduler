from rest_framework import serializers 
from scheduler.models import Scheduler
 
 
class SchedulerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Scheduler
        fields = ('schedulerID',
                  'alarm')