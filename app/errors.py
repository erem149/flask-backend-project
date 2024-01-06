from app import app, db
from flask import render_template

@app.error_handler(404)
def not_found(error):
    return render_template('404.html'), 404