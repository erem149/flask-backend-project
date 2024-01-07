from app import app, db
from app.models import User

@app.shell_context_processor
def make_shell_content():
    return dict(db=db, User=User)