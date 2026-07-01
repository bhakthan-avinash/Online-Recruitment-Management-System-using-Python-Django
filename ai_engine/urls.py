from django.urls import path
from .views import upload_resume, job_match_view

urlpatterns = [
    path('', upload_resume, name='upload_resume'),
    path('match/', job_match_view, name='job_match'),
]