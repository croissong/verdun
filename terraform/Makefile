DRONE_SERVER := "https://cloud.drone.io"
DRONE_TOKEN := $(shell sops -d --extract '["drone"]["token"]' secrets.yml)

check-vars:
	@test $(do_token) || (echo 'do_token is not defined' && exit 1)
	@test $(github_token) || (echo 'github_token is not defined' && exit 1)

init:
	terraform init

plan: init
	terraform plan -var "do_token=$(do_token)" -var "gh_token=$(gh_token)"

apply: init
	DRONE_SERVER=$(DRONE_SERVER) DRONE_TOKEN=$(DRONE_TOKEN) terraform apply -var "do_token=$(do_token)" -var "gh_token=$(gh_token)" 

tf-provider-circleci:
	cd plugin_repos/terraform-provider-circleci
	make install_plugin_locally TERRAFORM_PLUGIN_DIR=$PWD/../../.terraform/plugins/linux_amd64
	cd -
	terraform init

do-get-k8s-versions:
	curl -s -H "Authorization: Bearer $(do_token)" "https://api.digitalocean.com/v2/kubernetes/options" | jq '.options.versions'

delete-acme-records:
	for f in $(doctl compute domain records list patrician.gold | tail -n+2 | grep '_acme-challenge' | awk '{print $1}'); do doctl compute domain records delete patrician.gold "$f"; done
