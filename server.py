from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
current_dir = os.getcwd()

teaching_file = open(current_dir+'/data/teaching.json')
content = json.load(teaching_file)
teaching_file.close()

quiz_file = open(current_dir+'/data/quiz.json')
questions = json.load(quiz_file)
quiz_file.close()


@app.route('/', )
def home():
    return render_template('Home.html')


@app.route('/learn/<page>')
def teaching_blinds(page):
    return render_template("learn.html", content=content[page], total=len(content))


@app.route('/quiz/<page>')
def quiz_page(page):
    return render_template("quiz.html", question=questions[page], total=len(questions), index=int(page))


@app.route('/results')
def results():
    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug=True)
