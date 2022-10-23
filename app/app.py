from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from services.service import factorial as f

from observability.counter import REQUEST_COUNTER

app = Flask(__name__)
metrics = PrometheusMetrics(app=app, path="/metrics")


@app.route("/fact")
def factorial():
    try:
        fac = f(n=int(request.args.get("n")))
        REQUEST_COUNTER.labels(status=200).inc()
        return jsonify({"result": fac})
    except:
        REQUEST_COUNTER.labels(status=500).inc()
        return jsonify({"result": "error"})
