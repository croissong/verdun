kubeconf = $(PWD)/kubeconfig.yml

get-kubeconf:
	@test $(cluster_id) || (echo 'cluster_id is not defined' && exit 1)
	@curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/clusters/$(cluster_id)/kubeconfig" -o $(kubeconf)
	ls -al $(kubeconf)

check-vars:
	@test $(kubectx) || (echo 'kubectx is not defined' && exit 1)

sync: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile sync

apply: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile apply

diff: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile diff

status: check-vars
	KUBECONFIG=$(kubeconf) KUBECONTEXT=$(kubectx) helmfile status

# TODO change to helm chart https://github.com/kubedb/project/issues/522
kubedb:
	curl -fsSL https://raw.githubusercontent.com/kubedb/cli/0.12.0/hack/deploy/kubedb.sh \
		| bash -s -- --namespace=kubedb --rbac
