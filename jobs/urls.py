from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('post-job/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path(
    'recruiter-dashboard/',
    views.recruiter_dashboard,
    name='recruiter_dashboard'
),

path(
    'delete-job/<int:job_id>/',
    views.delete_job,
    name='delete_job'
),
path(
    'candidate-dashboard/',
    views.candidate_dashboard,
    name='candidate_dashboard'
),
]