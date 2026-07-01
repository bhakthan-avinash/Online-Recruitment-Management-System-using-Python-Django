from django.shortcuts import render
from .forms import ResumeUploadForm
from .utils.resume_parser import extract_text_from_pdf
from .utils.resume_analyzer import analyze_resume
from .utils.skill_extractor import extract_skills
from .utils.job_matcher import calculate_match

def upload_resume(request):
    analysis = None

    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save()

            resume_text = extract_text_from_pdf(resume.resume.path)
            analysis = analyze_resume(resume_text)

    else:
        form = ResumeUploadForm()

    return render(request, 'ai_engine/resume_upload.html', {
        'form': form,
        'analysis': analysis
    })
def job_match_view(request):
    result = None

    if request.method == 'POST':
        resume_text = request.POST.get('resume_text')
        job_description = request.POST.get('job_description')

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        result = calculate_match(resume_skills, job_skills)

    return render(request, 'ai_engine/job_match.html', {
        'result': result
    })