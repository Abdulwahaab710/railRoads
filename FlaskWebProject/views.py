"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, request
import db
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
    return render_template('survey.html', questions=db.fetchQuestion())

@app.route('/submitQuestionnaire', methods=['GET', 'POST'])
def submitQuestionnaire():
    if request.method == 'POST':
        return str( [ v for v in request.form.values()  ] )

@app.route('/requests/<q>', methods=['GET', 'POST'])
def req(q):
    return 'hello world ' + q
