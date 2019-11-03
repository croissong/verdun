# traefik
```
rm -fr traefik && curl https://codeload.github.com/containous/traefik-helm-chart/tar.gz/master | tar -xz && mv traefik-helm-chart-master traefik
```

# ingress-monitor-controller
```
rm -r ingressmonitorcontroller && curl https://codeload.github.com/stakater/IngressMonitorController/tar.gz/master | \
  tar -xz --strip=4 IngressMonitorController-master/deployments/kubernetes/chart/ingressmonitorcontroller
```
