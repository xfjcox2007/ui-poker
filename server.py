from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
current_dir = os.getcwd()
teaching_file = open(current_dir+'/data/teaching.json')
content = json.load(teaching_file)
teaching_file.close()

@app.route('/', )
def home():
    return render_template('Home.html')

@app.route('/learn/1')
def teaching_blinds():
    return render_template("learn_blinds.html", content=content["1"])

if __name__ == '__main__':
    app.run(debug=True)
