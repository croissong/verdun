from os import environ, path
from subprocess import run
from base64 import b64decode

kubectx = environ['K8S_CLUSTER_CONTEXT']
do_token = environ['DO_TOKEN_GET_KUBECONF']
cluster_id = environ['DO_K8S_CLUSTER_ID']
key_b64 = environ['HELM_GPG_KEY_B64']

def main():
    import_gpg_key()
    get_kubeconfig()
    helm_init()
    run(f'make apply kubectx={kubectx}'.split(), check=True, cwd='k8s')

def import_gpg_key():
    key = b64decode(key_b64)
    run('gpg --import'.split(), input=key, check=True)
    run('gpg --list-secret-keys'.split())

def get_kubeconfig():
    cmd = f'make get-kubeconf do_token={do_token} cluster_id={cluster_id}'
    run(cmd.split(), cwd='k8s', check=True)
    environ["KUBECONFIG"] = path.abspath('kubeconfig.yml')

def helm_init():
    run('helm init --client-only'.split(), check=True)
    run('helm version'.split(), check=True)
    run('helmfile -v'.split(), check=True)

if __name__ == "__main__":
    main()
