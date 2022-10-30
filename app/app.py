import os

from flask import Flask
from . import db

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    db_conn = db.get_db()
    items = db_conn.execute(
        ' SELECT id, name '
        ' FROM record '
        ' ORDER BY id DESC ').fetchall()
    result = ""
    for item in items:
        result += item["name"] + "\n"

    return result


@app.route('/save')
def save():
    db_conn = db.get_db()

    db_conn.execute(
        'INSERT INTO record (name) '
        'VALUES (?) ',
        'D'
    )
    db_conn.commit()
    return 'Record saved'


if __name__ == '__main__':
    app.run()
