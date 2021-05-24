from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods = ['GET'])
def runApp():
    return jsonify({'greetings' : 'hello world'})

if __name__ == "__main__":
    app.run(host='127.0.0.1')
