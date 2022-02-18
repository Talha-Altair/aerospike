from flask import Flask, render_template, jsonify, request
from time import sleep
import json

from connections import client, key

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/insert', methods=['POST', 'GET'])
def insert():

    (key_meta, meta, data) = client.get(key)

    print(data)

    data['tasks'].append(json.loads(request.get_data()))

    client.put(key, data)

    print(data)

    return 'Inserted'


@app.route('/all')
def all():

    (key_meta, meta) = client.exists(key)

    if not meta:

        client.put(key, {'tasks': []})

    (key_meta, meta, data) = client.get(key)

    print(data)

    return jsonify(data)


if __name__ == '__main__':

    sleep(10)

    client.connect()

    app.run(debug=True, host='0.0.0.0', port=8080)
