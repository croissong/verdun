kubeconf:
	$(eval clusterid=$(shell sh -c 'cd ../terraform && terraform output cluster_id && cd ../k8s'))
	$(eval KUBECONFIG=$(PWD)/kubeconfig.yml)
	curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/clusters/$(clusterid)/kubeconfig" > $(KUBECONFIG)

kubectx:
	$(eval KUBECONTEXT=$(shell sh -c 'cd ../terraform && terraform output cluster_context && cd ../k8s'))

apply: kubeconf kubectx
	KUBECONTEXT=$(KUBECONTEXT) helmfile apply
