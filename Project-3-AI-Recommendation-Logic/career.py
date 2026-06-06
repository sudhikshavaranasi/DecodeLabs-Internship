careers = {
    "AI Engineer": ["python", "machine learning", "data science"],
    "Web Developer": ["html", "css", "javascript"],
    "Cyber Security Analyst": ["networking", "security", "linux"],
    "Software Engineer": ["coding", "problem solving", "algorithms"],
    "Data Analyst": ["excel", "statistics", "sql"]
}

user_input = input(
    "Enter your skills/interests (comma separated): "
).lower()

user_skills = [skill.strip() for skill in user_input.split(",")]

scores = {}

for career, skills in careers.items():
    score = 0

    for skill in user_skills:
        if skill in skills:
            score += 1

    scores[career] = score

recommendations = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Careers:\n")

found = False

for career, score in recommendations:
    if score > 0:
        print(f"{career} (Match Score: {score})")
        found = True

if not found:
    print("No suitable career found. Try entering different skills.")
