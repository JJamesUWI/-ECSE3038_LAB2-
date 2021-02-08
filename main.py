from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

USER = {
    "success": True,
    "data": {
        "last_updated": "7/2/2021, 12:50:00",
        "username": "James",
        "role": "Junior Engineer",
        "color": "Grey"
    }
}


TANK = {}
id_count = 0


@app.route("/")
def home():
    return "ECSE3038 - Lab 2"


@app.route("/profile", methods=["GET"])
def get_profile():
    return jsonify(USER)


@app.route("/profile", methods=["POST"])
def post_profile():
    # Get date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")

    USER[0]["data"]["last_updated"] = (dt)
    USER[0]["data"]["username"] = (request.json["username"])
    USER[0]["data"]["role"] = (request.json["role"])
    USER[0]["data"]["color"] = (request.json["color"])

    return jsonify(USER)


@app.route("/profile", methods=["PATCH"])
def patch_profile():
    # Get date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")

    USER[0]["data"]["last_updated"] = (dt)
    BUF = request.json

    if "username" in BUF:
        USER[0]["data"]["username"] = (BUF["username"])
    if "role" in BUF:
        USER[0]["data"]["role"] = (BUF["role"])
    if "color" in BUF:
        USER[0]["data"]["color"] = (BUF["color"])

    return jsonify(USER)


@app.route("/data")
def get_data():
    return jsonify(TANK)


@app.route("/data", methods=["POST"])
def post_data():
    global id_count
    id_count += 1
    t = {}
    t = request.json
    t["id"] = id_count
    TANK.append(t)
    return jsonify(t)


@app.route('/data/<int:id>', methods=["PATCH"])
def patch_data(id):
    tank_data = request.json

    for itemss in TANK:
        if itemss["id"] == id:
            itemss["location"] = tank_data["location"]
            itemss["lat"] = tank_data["lat"]
            itemss["long"] = tank_data["long"]
            itemss["percentage_full"] = tank_data["percentage_full"]
            break
    return jsonify(TANK[id-1])


@app.route('/data/<int:id>', methods=["DELETE"])
def delete_data(id):
    TANK.remove(TANK[id-1])
    DEL1 = {
        "success": True,
    }
    return jsonify(DEL1)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )
