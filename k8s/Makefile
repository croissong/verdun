kubeconf = $(PWD)/kubeconfig.yml

get-kubeconf:
	@test $(DO_TOKEN) || (echo 'DO_TOKEN is not defined' && exit 1)
	@test $(CLUSTER_ID) || (echo 'CLUSTER_ID is not defined' && exit 1)
	@curl -s -H "Authorization: Bearer $(DO_TOKEN)" "https://api.digitalocean.com/v2/kubernetes/clusters/$(CLUSTER_ID)/kubeconfig" -o $(kubeconf)

check-vars:
	@test $(kubectx) || (echo 'kubectx is not defined' && exit 1)

sync: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile sync --concurrency=1

apply: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile apply --concurrency=1

diff: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile diff --concurrency=1

status: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile status
