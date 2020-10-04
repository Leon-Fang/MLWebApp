from django.urls import path
from . import views

urlpatterns = [
    path('',views.calendarP,name="calendarP")
]
