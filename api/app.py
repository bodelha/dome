from flask import Flask
from controllers.v1.measurements import save_measurements, get_measurements
from controllers.v1.sensor_data import get_sensor_data
from controllers.v1.health_check import health_check
from db import Database

app = Flask(__name__)
db = Database()


app.route("/v1/measurements", methods=["POST"])(save_measurements)
app.route("/v1/measurements", methods=["GET"])(get_measurements)
app.route("/v1/sensor-data", methods=["GET"])(get_sensor_data)
app.route("/", methods=["GET"])(health_check)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
