plan:
	terraform plan -var "do_token=$(do_token)" -var "circleci_token=$(circleci_token)" -var "do_token_get_kubeconf=$(do_token_get_kubeconf)"

apply:
	terraform apply -var "do_token=$(do_token)" -var "circleci_token=$(circleci_token)" -var "do_token_get_kubeconf=$(do_token_get_kubeconf)"

tf-provider-circleci:
	cd plugin_repos/terraform-provider-circleci
	make install_plugin_locally TERRAFORM_PLUGIN_DIR=$PWD/../../.terraform/plugins/linux_amd64
	cd -
	terraform init
