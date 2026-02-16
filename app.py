from flask import Flask, render_template, request

app = Flask(__name__)

REQUIRED_SKILLS = ["Python", "Statistics", "Machine Learning", "SQL"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_skills = request.form.get("skills")
    user_skills = [skill.strip() for skill in user_skills.split(",")]

    missing = []

    for skill in REQUIRED_SKILLS:
        if skill not in user_skills:
            missing.append(skill)

    return render_template("index.html", missing=missing)

if __name__ == "__main__":
    app.run(debug=True)