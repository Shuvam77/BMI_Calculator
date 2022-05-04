from django import views
from django.urls import path
from .views import indexView


urlpatterns = [
    path('', indexView.as_view(), name="index-view")
]


