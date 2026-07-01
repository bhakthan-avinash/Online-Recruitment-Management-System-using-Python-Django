import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
def generate_question(role):
    prompt = f"""
    Generate one technical interview question for a {role} candidate.
    Only return the question.
    """

    response = model.generate_content(prompt)
    return response.text
def evaluate_with_ai(role, question, answer):
    prompt = f"""
    Evaluate the candidate answer.

    Role: {role}
    Question: {question}
    Candidate Answer: {answer}

    Return:
    1. Technical Score (out of 10)
    2. Communication Score (out of 10)
    3. Feedback
    4. Improvement Suggestions
    """

    response = model.generate_content(prompt)
    return response.text