def calculate_match(resume_skills, job_skills):
    matched = set(resume_skills).intersection(set(job_skills))
    score = (len(matched) / len(job_skills)) * 100

    missing = set(job_skills) - set(resume_skills)

    return {
        "score": round(score, 2),
        "matched": list(matched),
        "missing": list(missing)
    }