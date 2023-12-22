import os
from flask import Flask, jsonify, render_template
from . import db

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
    # TEMPLATE_FOLDER=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lecturer')
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
    return render_template('lecturer/index.html')

if __name__ == '__main__':
    app.run()
