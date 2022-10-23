build:
	@docker build -t aminehajali/factorial ./app

push: build
	@docker push aminehajali/factorial

create-local-cluster:
	@kind create cluster
	@kubectl cluster-info --context kind-kind

delete-local-cluster:
	@kind delete cluster

install-helms:
	@helm install prometheus prometheus-community/prometheus
	@helm install factorial ./app/chart

uninstall-helms:
	@helm uninstall prometheus
	@helm uninstall factorial

local-run:
	@docker compose up

clean:
	@find . -name "__pycache__" -exec rm -rf {} \; >> /dev/null
