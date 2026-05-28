from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm


def home(request):

    jobs = Job.objects.all()

    return render(request, 'home.html', {
        'jobs': jobs
    })

@login_required
def post_job(request):

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.recruiter = request.user

            job.save()

            return redirect('/')

    else:

        form = JobForm()

    return render(request, 'post_job.html', {
        'form': form
    })