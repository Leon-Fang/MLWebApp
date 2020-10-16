from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='NewIndex'),
    path('<int:p1>/',views.index_page,name='NewIndex'),
]
