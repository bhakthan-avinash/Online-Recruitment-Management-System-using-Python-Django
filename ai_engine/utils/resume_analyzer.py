import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_resume(resume_text):
    prompt = f"""
    Analyze this resume and provide:
    1. Candidate Summary
    2. Skills Found
    3. Missing Skills
    4. ATS Score out of 100
    5. Recommended Roles

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)
    return response.text