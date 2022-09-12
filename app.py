from flask import Flask, request

app = Flask(__name__)
devices = []


@app.route('/device', methods=['POST'])
def create_device():
    if request.method == 'POST':
        app.logger.info(request.get_data())
        devices.append(request.get_json())
        return request.get_json()


@app.route('/device', methods=['PUT'])
def update_device():
    if request.method == 'PUT':
        app.logger.info(request.get_data())
        devices.append(request.get_json())
        return request.get_json()

@app.route('/clear', methods=['POST'])
def clear_device():
    if request.method == 'POST':
        app.logger.info(request.get_data())
        devices = []
        return devices


@app.route('/', methods=['GET'])
def device_info():
    if request.method == 'GET':
        app.logger.info(devices)
        return devices


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

