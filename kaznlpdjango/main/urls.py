from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tokenz', views.tokenz),
    path('normalize', views.normalize),
    path('morpholog', views.morphologic)
]
