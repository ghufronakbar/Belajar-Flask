# CREATE FLASK APP

## Install virtualenv globally
### pip install virtualenv

## Create virtualenv
### virtualenv venv

## Activate virtualenv
### venv/Scripts/activate

## Install Flask
### pip install flask

## Run Flask
### flask run

## Source Code:
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()