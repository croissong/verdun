init:
	terraform init

check-vars:
	test $(do_token)
	test $(circleci_token)
	test $(do_token_get_kubeconf)

plan: check-vars init
	terraform plan -var "do_token=$(do_token)" -var "circleci_token=$(circleci_token)" -var "do_token_get_kubeconf=$(do_token_get_kubeconf)"

apply: check-vars init
	terraform apply -var "do_token=$(do_token)" -var "circleci_token=$(circleci_token)" -var "do_token_get_kubeconf=$(do_token_get_kubeconf)"

tf-provider-circleci:
	cd plugin_repos/terraform-provider-circleci
	make install_plugin_locally TERRAFORM_PLUGIN_DIR=$PWD/../../.terraform/plugins/linux_amd64
	cd -
	terraform init

do-get-k8s-versions:
	curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/options" | jq '.options.versions'

delete-acme-records:
	for f in $(doctl compute domain records list patrician.gold | tail -n+2 | grep '_acme-challenge' | awk '{print $1}'); do doctl compute domain records delete patrician.gold "$f"; done
