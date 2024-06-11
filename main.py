
from flask import Flask, render_template

app = Flask(__name__)

lessons = [
    {
        "number": 1,
        "title": "Introduction to Malayalam",
        "content": "In this lesson, you will learn the basics of Malayalam, including the alphabet, pronunciation, and grammar.",
    },
    {
        "number": 2,
        "title": "Malayalam Vocabulary",
        "content": "In this lesson, you will learn common Malayalam vocabulary, including greetings, numbers, and everyday objects.",
    },
    {
        "number": 3,
        "title": "Malayalam Grammar",
        "content": "In this lesson, you will learn the basics of Malayalam grammar, including sentence structure, verb conjugations, and noun declensions.",
    },
]

@app.route("/")
def index():
    return render_template("index.html", lessons=lessons)

@app.route("/lessons")
def lessons():
    return render_template("lessons.html", lessons=lessons)

@app.route("/lesson/<int:lesson_number>")
def lesson(lesson_number):
    lesson = next((lesson for lesson in lessons if lesson["number"] == lesson_number), None)
    if lesson:
        return render_template("lesson.html", lesson=lesson)
    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
