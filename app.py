from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask App!")

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
