from flask import Flask
import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Main request successful!")
    return "Hello World!"

@app.route("/health")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("Health check called successfully")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success", "code": 0, "data": {"userCount": 140, "userCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("Metrics endpoint called successfully")
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
