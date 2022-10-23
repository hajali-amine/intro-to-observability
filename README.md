# Introduction to Observability

This repository is a playground to test the following tools:

- Prometheus
- Grafana
- Node Exporter
- Helm

## How does it work

### Part I

The first part consists of a small service that computes the factorial of a number n.
We added a __Counter__ metric to it that counts the number of successful requestes to that service.
We then exposed the __GET /metrics__ endpoint to get the metrics of our application.
Then we configured __Prometheus__ to pull these metrics regularily.
Then we used Node Exporter to get our machine's metrics and visualized them in a Grafana dashboard.#
All of these things were run using docker containers.

### Part II

Now we want to have the same process using k8s and Helm.
First, we need to add the repo reference, thus we run the following command;

``` shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

Then we prepare our application's chart.
Then we apply them and congrats you got yourself an observed service!

### And that's all folks
