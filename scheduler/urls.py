from django.conf.urls import url 
from scheduler import views 
 
urlpatterns = [ 
    url(r'^api/scheduler$', views.scheduler_list),
    url(r'^api/scheduler/(?P<pk>[0-9]+)$', views.scheduler_detail),
    url(r'^api/scheduler/published$', views.scheduler_list_published)
]