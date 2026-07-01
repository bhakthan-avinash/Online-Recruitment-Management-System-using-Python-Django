from django.shortcuts import render
from .forms import ResumeUploadForm
from .utils.resume_parser import extract_text_from_pdf
from .utils.resume_analyzer import analyze_resume

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