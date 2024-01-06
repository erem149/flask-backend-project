from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello people with the spirit of learning!~ "