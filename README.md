# Introduction to Observability

This repository is a playground to test the following tools:

- Prometheus
- Grafana
- Node Exporter

## How does it work

The first part consists of a small service that computes the factorial of a number n.
We added a __Counter__ metric to it that counts the number of successful requestes to that service.
We then exposed the __GET /metrics__ endpoint to get the metrics of our application.
Then we configured __Prometheus__ to pull these metrics regularily.

Then we used Node Exporter to get our machine's metrics and visualized them in a Grafana dashboard.

### And that's all folks
