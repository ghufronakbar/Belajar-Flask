# STATIC FLASK APP

## Structure Directory
```
my_flask_app/
│
├── venv/                 # Virtual environment
│
├── app.py                # File utama aplikasi Flask
│
├── static/               # Folder untuk file statis (CSS, JS, gambar, dll)
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/            # Folder untuk file template (HTML)
    └── index.html

```

## Example Source Code:
```
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
```