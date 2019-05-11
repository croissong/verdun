kubeconf = $(PWD)/kubeconfig.yml

get-kubeconf:
	@test $(cluster_id) || (echo 'cluster_id is not defined' && exit 1)
	@curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/clusters/$(cluster_id)/kubeconfig" > $(kubeconf)

check-vars:
	@test $(kubectx) || (echo 'kubectx is not defined' && exit 1)

sync: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile sync

diff: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile diff

status: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile status
