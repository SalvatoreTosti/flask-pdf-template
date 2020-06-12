from app import app
from app.interfaces import pdf
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
