init:
	terraform init

plan: init
	terraform plan

apply: init
	terraform apply

delete-acme-records:
	for f in $(doctl compute domain records list patrician.cloud | tail -n+2 | grep '_acme-challenge' | awk '{print $1}'); do doctl compute domain records delete patrician.cloud "$f"; done

delete-volumes:
	#todo
