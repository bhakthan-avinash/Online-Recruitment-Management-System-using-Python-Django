from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job, Application
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
@login_required
def apply_job(request, job_id):

    job = Job.objects.get(id=job_id)

    if request.method == 'POST':

        resume = request.FILES.get('resume')

        already_applied = Application.objects.filter(
            candidate=request.user,
            job=job
        ).exists()

        if not already_applied:

            Application.objects.create(
                candidate=request.user,
                job=job,
                resume=resume
            )

        return redirect('/candidate-dashboard/')

    return render(request,
        'apply_job.html',
        {
            'job': job
        }
    )
@login_required
def recruiter_dashboard(request):

    jobs = Job.objects.filter(
        recruiter=request.user
    )

    return render(request,
        'recruiter_dashboard.html',
        {
            'jobs': jobs
        }
    )
@login_required
def delete_job(request, job_id):

    job = Job.objects.get(id=job_id)

    if job.recruiter == request.user:

        job.delete()

    return redirect('/recruiter-dashboard/')
@login_required
def candidate_dashboard(request):

    applications = Application.objects.filter(
        candidate=request.user
    )

    return render(
        request,
        'candidate_dashboard.html',
        {
            'applications': applications
        }
    )