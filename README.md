# Flask

```CMD
- To create directory/Folder = `mkdir <name>`
- To remove directory/Folder = `rmdir <name>`
- To create file = `type nul > app.py`
- to create file using CMD/Powershell : `type <filename> (type template.py)`


```

## Vertual environment related shortcuts

- To create environment = `conda create -p flask_env -y`
- To check available envs = `conda env list`
- To check available envs = `conda info --envs`
- To activate environment = `conda activate flask_env`
- To install requirements.txt = `pip install -r requirements.txt`

## Package related shortcuts

- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To check python installed version = `python --version`


## Git Command

- To add all file = `git add .`

- To add any particular file = `git add <file_name>`

- To commit = `git commit -m "commit message"`

- To push the code = `git push origin main`

## Docs:

Flask docs : `https://flask.palletsprojects.com/en/stable/`
Flask Quickstart : `https://flask.palletsprojects.com/en/stable/quickstart/`
Flask blueprint : `https://flask.palletsprojects.com/en/stable/blueprints/`


### A minimal Flask application code:

```flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

### Basic app.py

```
app = Flask(__name__)

@app.route('/')
def index():
    return "Home page"

@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return "Contact Us"
```


- To set the file as Flask app to the environment variable = `set flask_app=app.py`
- To run the server = `flask run`
- To see the result on browser = `http://localhost:5000/`
- To set the flask on debug to auto reload = `set flask_debug=1`
