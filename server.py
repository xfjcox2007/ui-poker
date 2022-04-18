from flask import Flask, render_template, request
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

# user_details.id = uuid.uuid1()

user_log = [user]


@app.route('/', )
def home():
    user_log[0]["id"] = uuid.uuid4().int
    print(user_log[0])
    return render_template('Home.html')


@app.route('/learn/<page>')
def teaching_blinds(page):
    user_log[0]["learn"] = {page: datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")}
    return render_template("learn.html", content=content[page], total=len(content))


@app.route('/quiz/<page>')
def quiz_page(page):
    print(user_log[0])
    user_log[0]["quiz"].append({page: datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")})
    return render_template("quiz.html", question=questions[page], total=len(questions), index=int(page),
                           logs=user_log[0]["quiz"])


@app.route('/results')
def results():
    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug=True)
