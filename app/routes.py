from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return "Hello people with the spirit of learning!~ "
# # Try to see the difference between the two lines below
# return render_template('index.html')