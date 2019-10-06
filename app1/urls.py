
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('calculator/', views.calculator),
    path('about/', views.about)

]
