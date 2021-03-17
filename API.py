from flask import Flask ,request, jsonify
import json
from vitest import summary

response = ''

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def summarize():
    global response

    request_data = request.json
    text = request_data['text']
    text = summary(text)
    return  jsonify({'text' : text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)