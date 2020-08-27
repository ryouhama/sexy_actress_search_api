from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_sexy_actress, name='sexy_actress'),
]
