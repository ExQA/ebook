
from django.conf.urls import url, include
from . import  views
urlpatterns = [
    url(r'ˆ$', views.index),
    url(r'ˆcalculater/$', views.index),
    url(r'ˆabout/$', views.index)

]
