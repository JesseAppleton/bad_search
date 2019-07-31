
from django.urls import path
from apps.search import views

urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('real_search', views.real_search),
]
