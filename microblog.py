from app import app, db
from app.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return{'db':db, 'User':User, 'Post':Post}

def start_ngrok():
    from pyngrok import ngrok

    url = ngrok.connect(5000)
    print('* Tunnel URL', url)

if app.config['START_NGROK']:
    start_ngrok()