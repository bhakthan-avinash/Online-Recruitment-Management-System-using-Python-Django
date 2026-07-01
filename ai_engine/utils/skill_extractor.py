skills_db = [
    "python", "django", "flask", "sql",
    "mysql", "aws", "docker", "machine learning"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills