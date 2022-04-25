from flask import Flask, render_template, request, jsonify
import os
import json
import datetime
import uuid

app = Flask(__name__)
current_dir = os.getcwd()

teaching_file = open(current_dir + '/data/teaching.json')
content = json.load(teaching_file)
teaching_file.close()

quiz_file = open(current_dir + '/data/quiz.json')
questions = json.load(quiz_file)
quiz_file.close()

user_details = open(current_dir + '/data/user.json')
user = json.load(user_details)
user_details.close()

user_log = user


def prepareLogs():
    for index, question in enumerate(content):
        user_log["learningProgress"][str(question)] = {"startTime": "", "status": "NotStarted",
                                                       "topic": content[question]["topic"]}
    for index, question in enumerate(questions):
        user_log["quiz"][str(question)] = {"startTime": "", "QuestionNumber": question, "status": "NotStarted",
                                           "answer": ""}


@app.route('/', )
def home():
    user_log["id"] = uuid.uuid4().int
    prepareLogs()
    return render_template('Home.html')


@app.route('/learn/<page>')
def learn_page(page):
    user_log["learningProgress"][str(page)]["startTime"] = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
    user_log["learningProgress"][str(page)]["status"] = "completed"
    return render_template("learn.html",
                           content=content[page],
                           total=len(content))


@app.route('/quiz/<page>')
def quiz_page(page):
    user_log["quiz"][str(page)]["startTime"] = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
    user_log["quiz"][str(page)]["status"] = "unattempted"
    return render_template("quiz.html",
                           question=questions[page],
                           total=len(questions),
                           index=int(page),
                           logs=user_log["quiz"])


@app.route('/updateQuiz', methods=['post'])
def update_quiz():
    page = request.get_json()["page"]
    user_log["quiz"][page]["status"] = "attempted"
    user_log["quiz"][page]["answer"] = request.get_json()["selection"]
    return jsonify(user_log)


@app.route('/fetchData', methods=['get'])
def get_logs():
    return jsonify(user_log)


@app.route('/results')
def results():
    correct = 0
    answers = user_log['quiz']
    for i in range(1,len(answers)+1):
      if str(answers[str(i)]['answer']) == str(questions[str(i)]['answer']):
        correct += 1
    score = correct / len(answers)
    return render_template("results.html", score=int(round(score, 2) * 100))


if __name__ == '__main__':
    prepareLogs()
    app.run(debug=True)
