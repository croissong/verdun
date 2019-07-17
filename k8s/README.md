## Run apply
```
make apply kubectx=$KUBECONTEXT
```

## Cilium patch portmap conf to allow hostports
via https://github.com/snormore/cilium-portmap#deploy-as-an-initcontainer
```
kc edit ds -n kube-system cilium
# Insert initContainers *first* in list:
- name: cilium-portmap
  image: snormore/cilium-portmap-init
  imagePullPolicy: IfNotPresent
  volumeMounts:
  - mountPath: /host/etc/cni/net.d
    name: etc-cni-netd
```
