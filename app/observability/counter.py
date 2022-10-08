from prometheus_client import Counter

REQUEST_COUNTER = Counter("nb_request", "Request counter", ["status"])
