DRONE_SERVER := "https://cloud.drone.io"
DRONE_TOKEN := $(shell sops -d --extract '["drone"]["token"]' secrets.yml)

init:
	terraform init

plan: init
	terraform plan -var "do_token=$(do_token)" -var "drone_token=$(drone_token)" -var "do_token_get_kubeconf=$(do_token_get_kubeconf)" -var helm_gpg_key_b64=$(helm_gpg_key_b64) -var do_spaces_access_id=$(do_spaces_access_id) -var do_spaces_secret_key=$(do_spaces_secret_key) -var docker_user=$(docker_user) -var docker_password_b64=$(docker_password_b64)

apply: init
	DRONE_SERVER=$(DRONE_SERVER) DRONE_TOKEN=$(DRONE_TOKEN) terraform apply

tf-provider-circleci:
	cd plugin_repos/terraform-provider-circleci
	make install_plugin_locally TERRAFORM_PLUGIN_DIR=$PWD/../../.terraform/plugins/linux_amd64
	cd -
	terraform init

do-get-k8s-versions:
	curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/options" | jq '.options.versions'

delete-acme-records:
	for f in $(doctl compute domain records list patrician.gold | tail -n+2 | grep '_acme-challenge' | awk '{print $1}'); do doctl compute domain records delete patrician.gold "$f"; done
