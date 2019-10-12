from flask import Flask
from app.main.api import blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(blueprint)
    app.run(host='0.0.0.0')
