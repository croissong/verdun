# run it
```
make apply do_token=$(do_token) circleci_token=$(circleci_token) do_token_get_kubeconf=$(do_token_get_kubeconf) helm_gpg_key_b64=$(helm_gpg_key_b64)
```

# setup circleci terraform provider
```
make tf-provider-circleci
```
