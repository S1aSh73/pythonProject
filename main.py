# import main Flask class and request object
from flask import Flask, request
import json
import os

# create the Flask app
app = Flask(__name__)

@app.route('/device', methods=['GET', 'POST', 'PUT'])
def device():
    device_info = []
    if request.method == 'POST':
        with open('data.json', 'a') as outfile:
            json.dump(request.get_json(), outfile)
            outfile.write('\n')
        return request.get_json()
    if request.method == 'GET':
        with open('data.json') as outfile:
            [device_info.append(line.strip().replace('"', '')) for line in outfile.readlines()]
#            data = outfile.readline()
        return device_info
    if request.method == 'PUT':
        with open('data.json', 'a') as outfile:
            json.dump(request.get_json(), outfile)
            outfile.write('\n')
        return request.get_json()
    return 'Incorrect request'

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        pwd = os.getcwd()
        os.remove(f"{pwd}\data.json")
        return 'ok'
    return 'Incorrect request'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
