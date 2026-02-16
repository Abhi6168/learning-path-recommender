from flask import Flask, render_template, request

app = Flask(__name__)
SKILL_TIME = {
    "Python": 30,
    "Statistics": 25,
    "SQL": 20,
    "Machine Learning": 40,
    "Linear Algebra": 20,
    "Deep Learning": 45,
    "HTML": 15,
    "CSS": 15,
    "JavaScript": 30,
    "React": 35
}

# Career skill requirements
CAREER_PATHS = {
    "data scientist": ["Python", "Statistics", "SQL", "Machine Learning"],
    "machine learning engineer": ["Python", "Linear Algebra", "Machine Learning", "Deep Learning"],
    "web developer": ["HTML", "CSS", "JavaScript", "React"]
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    career = request.form.get("career")
    user_input = request.form.get("skills")

    if not career or not user_input:
        return render_template("index.html")

    career = career.lower()
    user_skills = [skill.strip().lower() for skill in user_input.split(",")]

    if career not in CAREER_PATHS:
        return render_template("index.html", error="Career not found")

    required_skills = CAREER_PATHS[career]

    missing_skills = []
    
    for skill in required_skills:
        if skill.lower() not in user_skills:
            missing_skills.append(skill)
    total_days=0
    for skill in missing_skills:
        total_days += SKILL_TIME.get(skill, 20)

    return render_template("index.html",
                       career=career.title(),
                       missing=missing_skills,
                       time=total_days)

if __name__ == "__main__":
    app.run(debug=True)
