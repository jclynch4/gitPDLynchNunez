from django.urls import path
from . import views

urlpatterns = [
    path('', views.tastecuba, name='tastecuba'),
    path('people', views.people, name='people'),
    path('origins', views.origins, name='origins'),
    path('nature', views.nature, name='nature'),
    path('join', views.join, name='join'),
    path('create_account', views.create_account, name='create_account'),

]
