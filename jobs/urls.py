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
path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
),

path(
    'delete-application/<int:application_id>/',
    views.delete_application,
    name='delete_application'
),
path(
    'view-applicants/<int:job_id>/',
    views.view_applicants,
    name='view_applicants'
),

path(
    'shortlist/<int:application_id>/',
    views.shortlist_candidate,
    name='shortlist_candidate'
),
]