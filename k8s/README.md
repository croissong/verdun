# Update kubeconfig & kubecontext
```
make kubeconfig do_token=$(do_token)
export KUBECONFIG=$PWD/kubeconfig.yml
export KUBECONTEXT=$(cd ../terraform && terraform output cluster_context && cd ../k8s)
```

# Run apply
```
make apply do_token=$(do_token)
```
