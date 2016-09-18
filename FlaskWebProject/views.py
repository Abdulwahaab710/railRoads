"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, request
import sqlite3
# import db
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/survey')
def survey():
    conn = sqlite3.connect('dataBase.db')
    result = []
    c = conn.cursor()
    c.execute('SELECT * FROM questions')
    for row in c:
        result.append(row)
    return render_template('survey.html', questions=result)

@app.route('/submitQuestionnaire', methods=['GET', 'POST'])
def submitQuestionnaire():
    # if request.method == 'POST':
        # return str( [ v for v in request.form.values()  ] )
    return '200'

@app.route('/requests/<q>', methods=['GET', 'POST'])
def req(q):
    return 'hello world ' + q
