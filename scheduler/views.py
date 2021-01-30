from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from scheduler.models import Scheduler
from scheduler.serializers import SchedulerSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def scheduler_list(request):
    # GET list of schedule, POST a new schedule, DELETE all schedule
    if request.method == 'GET':
        scheduler = Scheduler.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            scheduler = scheduler.filter(title__icontains=title)
        
        scheduler_serializer = SchedulerSerializer(scheduler, many=True)
        return JsonResponse(scheduler_serializer.data, safe=False)
        # 'safe=False' for objects serialization 
    elif request.method == 'POST':
        scheduler_data = JSONParser().parse(request)
        scheduler_serializer = SchedulerSerializer(data=scheduler_data)
        if scheduler_serializer.is_valid():
            scheduler_serializer.save()
            return JsonResponse(scheduler_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(scheduler_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Scheduler.objects.all().delete()
        return JsonResponse({'message': '{} Scheduler were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def scheduler_detail(request, pk):
    # find scheduler by pk (id)
    try: 
        scheduler = Scheduler.objects.get(pk=pk) 
    except Scheduler.DoesNotExist: 
        return JsonResponse({'message': 'The scheduler does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE scheduler
    if request.method == 'GET': 
        scheduler_serializer = SchedulerSerializer(scheduler) 
        return JsonResponse(scheduler_serializer.data)
    elif request.method == 'PUT': 
        scheduler_data = JSONParser().parse(request) 
        scheduler_serializer = SchedulerSerializer(scheduler, data=scheduler_data) 
        if scheduler_serializer.is_valid(): 
            scheduler_serializer.save() 
            return JsonResponse(scheduler_serializer.data) 
        return JsonResponse(scheduler_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        scheduler.delete() 
        return JsonResponse({'message': 'scheduler was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def scheduler_list_published(request):
    # GET all published schedulers
    scheduler = Scheduler.objects.filter(published=True)
        
    if request.method == 'GET': 
        scheduler_serializer =  SchedulerSerializer(scheduler, many=True)
        return JsonResponse(scheduler_serializer.data, safe=False)

# @api_view(['GET'])
# def hello(request):
#     # GET all published tutorials
#     return JsonResponse({'message': ' 1'}, status=status.HTTP_200_OK)
        