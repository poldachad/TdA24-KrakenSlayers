import os
from flask import Flask, jsonify, render_template, url_for
from . import db
import json

app = Flask(__name__, static_folder='static')

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite')
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)


@app.route('/')
def hello_world():
    return render_template('home/index.html')

@app.route('/api')
def api():
    secret = {"secret": "The cake is a lie"}
    return jsonify(secret)

@app.route('/lecturer')
def lecturer_page():
    json_file_path = os.path.join(os.getcwd(), 'app', 'static', 'lecturer.json') # absolute path to the json file
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)
    return render_template('lecturer/index.html', lecturer = json_data)

if __name__ == '__main__':
    app.run()
