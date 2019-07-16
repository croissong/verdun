#  traefik-fork
## Why?
- disable ingress
- custom traefik config templates
## Rebase
```
rm -fr traefik-fork && helm fetch --untar --untardir traefik-fork-tmp 'stable/traefik' && mv traefik-fork-tmp/traefik traefik-fork && rm -r traefik-fork-tmp
```
