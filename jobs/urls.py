from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('post-job/', views.post_job, name='post_job'),
]