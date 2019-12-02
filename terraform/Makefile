init:
	terraform init

plan: check-vars init
	terraform plan

apply: check-vars init
	terraform apply

check-vars:
	@test -n $(TF_VAR_do_token) || (echo 'TF_VAR_do_token must be defined' && exit 1)
	@test -n $(TF_VAR_gh_token) || (echo 'TF_VAR_gh_token must be defined' && exit 1)

delete-acme-records:
	for f in $(doctl compute domain records list patrician.cloud | tail -n+2 | grep '_acme-challenge' | awk '{print $1}'); do doctl compute domain records delete patrician.cloud "$f"; done

delete-volumes:
	#todo
