DRONE_SERVER := "https://cloud.drone.io"
DRONE_TOKEN := $(shell sops -d --extract '["drone"]["token"]' secrets.yml)

check-vars:
	@test $(do_token) || (echo 'do_token is not defined' && exit 1)
	@test $(gh_token) || (echo 'gh_token is not defined' && exit 1)

init:
	terraform init

plan: check-vars init
	@DRONE_SERVER=$(DRONE_SERVER) DRONE_TOKEN=$(DRONE_TOKEN) terraform plan -var "do_token=$(do_token)" -var "gh_token=$(gh_token)"

apply: check-vars init
	@DRONE_SERVER=$(DRONE_SERVER) DRONE_TOKEN=$(DRONE_TOKEN) terraform apply -var "do_token=$(do_token)" -var "gh_token=$(gh_token)" 

tf-provider-circleci:
	cd plugin_repos/terraform-provider-circleci
	make install_plugin_locally TERRAFORM_PLUGIN_DIR=$PWD/../../.terraform/plugins/linux_amd64
	cd -
	terraform init

delete-acme-records:
	for f in $(doctl compute domain records list patrician.cloud | tail -n+2 | grep '_acme-challenge' | awk '{print $1}'); do doctl compute domain records delete patrician.cloud "$f"; done

delete-volumes:
	#todo
