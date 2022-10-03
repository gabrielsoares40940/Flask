from flask import Flask
from flaskr.auth import bp as auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.config.from_object(__name__)


@app.route('/')
def hello():
    return 'Index Page'


app.run()
