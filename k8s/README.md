# Update kubeconfig & kubecontext
```
cluster_id=$(cd ../terraform && terraform output cluster_id && cd ../k8s)
make get-kubeconf do_token=$(do_token) cluster_id=$cluster_id
export KUBECONFIG=$PWD/kubeconfig.yml
export KUBECONTEXT=$(cd ../terraform && terraform output cluster_context && cd ../k8s)
```

# Run apply
```
make apply kubectx=$KUBECONTEXT
```
