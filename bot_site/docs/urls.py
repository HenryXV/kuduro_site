from django.urls import path
from . import views


app_name = 'docs'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('commands', views.CommandView.as_view(), name='command'),
]
