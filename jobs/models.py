from django.db import models
from django.conf import settings


class Job(models.Model):

    title = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    salary = models.CharField(max_length=50)

    description = models.TextField()

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
class Application(models.Model):

    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    resume = models.FileField(
    upload_to='resumes/',
    null=True,
    blank=True
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.candidate.username} applied for {self.job.title}"
