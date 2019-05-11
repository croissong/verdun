kubeconf:
	$(eval clusterid=$(shell sh -c 'cd ../terraform && terraform output cluster_id && cd ../k8s'))
	$(eval KUBECONFIG=$(PWD)/kubeconfig.yml)
	curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/clusters/$(clusterid)/kubeconfig" > $(KUBECONFIG)

kubectx:
	export KUBECONTEXT=$(cd ../terraform && terraform output cluster_context && cd ../k8s)

apply: kubeconf kubectx
	helmfile apply
