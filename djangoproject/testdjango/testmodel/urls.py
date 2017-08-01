from django.conf.urls import url
from .views import  index,adddb
from . import views
urlpatterns=[
    url('index/',index,name='index'),
    url(r'adddb',adddb,name='adddb'),
    url(r'private',views.private),
    url(r'allname',views.allname,name='allname')
]