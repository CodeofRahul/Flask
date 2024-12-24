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

- Flask docs : `https://flask.palletsprojects.com/en/stable/`
- Flask Quickstart : `https://flask.palletsprojects.com/en/stable/quickstart/`
- Flask blueprint : `https://flask.palletsprojects.com/en/stable/blueprints/`
- Flask Rendering Templates: `https://www.geeksforgeeks.org/flask-rendering-templates/`


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


## Jinja2:

- Jinja2 is a template processing toolkit
- Allows you to create and render text templates
- Integrates well with Flask
    - Use to render HTML based on templates

### Tags:

- `{% ... %}` for Statements
- `{{ ... }}` for Expressions to print variable
- `{# ... #}` for Comments not included in the template output

#### Conditoinal:

```
{% if ... %}
 ...
{% else %}
 ...
{% endif %}
```

```
{% if score > 80 %}
I'm happy to inform you that you did very well on todays {{ test_name }}.
{% else %}
Your score on today's test {{ test_name }} could have been better. More stduy.
{% endif %}
YOu achieved {{ score }} out of {{ max_score }} points!
```

#### Loops:

```
{% for ... %}
... 
{% endfor %}
```

```
topItems = ["Item 2", "Item 3", "Item 7"]

{% for item in topItems %}
{{item}}
{% endfor %}
```

