from django.db import models

# Create your models here.
from django.db import models

class ResumeUpload(models.Model):
    name = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)