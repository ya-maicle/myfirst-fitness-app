# controllers.py
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from openai_api import generate_workout

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fitnessLevel = request.form.get('fitnessLevel')
        equipment = request.form.get('equipment')
        response_json = generate_workout(fitnessLevel, equipment)
        if response_json is not None:
            session['response_json'] = response_json
            return redirect(url_for('response'))
        else:
            return "There was an error decoding the JSON response from GPT-3 after 3 attempts."
    return render_template('index.html')

@app.route('/response')
def response():
    data = session.get('response_json', {})
    return render_template('response.html', data=data)
