from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def basic_api():
    return Response(response={'result':'ok'}, status=200, mimetype='application/json')
@app.route("/test", methods=['POST','GET'])
def basic_api():
    return Response(response={'result':'ok'}, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)