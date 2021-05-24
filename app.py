# from flask import Flask, jsonify, request
# from flask_cors import CORS

# app = Flask(__name__)
# cors = CORS(app)

# @app.route('/', methods = ['GET'])
# def runApp():
#     return jsonify({'greetings' : 'hello world'})

# if __name__ == "__main__":
#     app.run(host='127.0.0.1')

import urllib.request
import json
import os
import ssl

from flask import Flask, jsonify, request
from flask_cors import CORS

# def runApp():
#     return 'Hello World'

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods = ['GET'])

# // Request data goes here
def requestModel():
    data = {
        "Inputs": {
            "WebServiceInput0":
            [
                {
                    'Quiz 1_Q1 Score': "false",
                    'Quiz 1_Q2 Score': "false",
                    'Quiz 1_Q3 Score': "false",
                    'Quiz 1_Q4 Score': "true",
                    'Quiz 1_Q5 Score': "true",
                    'Quiz 1_Q1 Time': "0",
                    'Quiz 1_Q2 Time': "1",
                    'Quiz 1_Q3 Time': "2",
                    'Quiz 1_Q4 Time': "1",
                    'Quiz 1_Q5 Time': "2",
                },
            ],
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'http://20.195.98.200:80/api/v1/service/model-decisiontree/score'
    api_key = 'fiUUUwL28J9AxzAbxB8gLmg3n4bcGEkJ' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))

if __name__ == "__main__":
    app.run(host='127.0.0.1')

