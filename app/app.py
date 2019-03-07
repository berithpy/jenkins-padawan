from flask import Flask, request, Response, jsonify
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def basic_api():
    return jsonify({'result': 'working!'})


@app.route("/test", methods=['POST', 'GET'])
def test_api():
    return jsonify({'test': 'test value'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
