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
    skills_required = models.TextField(
    null=True,
    blank=True
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
    candidate_skills = models.TextField(
    null=True,
    blank=True
    )

    match_score = models.IntegerField(
    default=0
    )
    status = models.CharField(
    max_length=20,
    default='Pending'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.candidate.username} applied for {self.job.title}"
