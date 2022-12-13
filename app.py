from flask import Flask, jsonify, request, abort
from chat import doChat

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def create_task():
    if not request.json or not 'q' in request.json:
        abort(400)
    q = request.json['q']
    print("q: " + q)
    r = doChat(q)
    print("r: " + str(r))
    return jsonify(r), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')