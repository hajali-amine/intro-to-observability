from flask import Flask, jsonify
from services.service import factorial as f
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from observability.counter import REQUEST_COUNTER

app = Flask(__name__)

@app.route("/<int(signed=True):n>")
def factorial(n):   
    try:
        fac = jsonify(f(n))
        REQUEST_COUNTER.labels(status=200).inc()
        return fac
    except:
        REQUEST_COUNTER.labels(status=500).inc()

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})