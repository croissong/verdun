kubeconf = $(PWD)/kubeconfig.yml

get-kubeconf:
	@test $(cluster_id) || (echo 'cluster_id is not defined' && exit 1)
	@curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/clusters/$(cluster_id)/kubeconfig" -o $(kubeconf)
	ls -al $(kubeconf)

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
