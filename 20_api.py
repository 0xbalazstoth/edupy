# Flask
# pip install flask
from flask import Flask, jsonify, request

app = Flask(__name__)

devices = []


@app.route("/")
def home():
    return {"message": "Hello, it is working."}


@app.route("/api/devices", methods=["GET"])
def get_devices():
    return jsonify(devices)


# Egy konkrét eszköz lekérése ID alapján
@app.route("/api/devices/<int:device_id>", methods=["GET"])
def get_device(device_id):
    device = next((device for device in devices if device["id"] == device_id), None)
    return jsonify(device) if device else ("", 404)


# Új eszköz hozzáadása
@app.route("/api/devices", methods=["POST"])
def add_device():
    new_device = request.get_json()
    new_device["id"] = devices[-1]["id"] + 1 if devices else 1
    devices.append(new_device)
    return jsonify(new_device), 201


# Eszköz törlése ID alapján
@app.route("/api/devices/<int:device_id>", methods=["DELETE"])
def delete_device(device_id):
    global devices
    devices = [device for device in devices if device["id"] != device_id]
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)
