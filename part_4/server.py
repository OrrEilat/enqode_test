import flask
import sqlite3
from q4config import *
# -----------------------------------

app = flask.Flask(__name__)

# initialize the database
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data_store (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# store endpoint
@app.route('/store', methods = ['POST'])
def store():
    data = flask.request.json
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data_store (data) VALUES (?)', [flask.json.dumps(data)])
        conn.commit()
        conn.close()
        return flask.jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        return flask.jsonify({'error': str(e)}), 500

# retrieve endpoint
@app.route('/retrieve', methods = ['GET'])
def retrieve():
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT data FROM data_store')
        rows = cursor.fetchall()
        conn.close()

        data = [flask.json.loads(row[0]) for row in rows]
        return flask.jsonify(data), 200
    except Exception as e:
        return flask.jsonify({'error': str(e)}), 500

# -----------------------------------
if __name__ == '__main__':
    init_db()
    app.run(host=ip, port=port)