from os import environ, path
from base64 import b64decode
from lib.util import is_local, run_cmd


def k8s():
    if is_local():
        return
    import_gpg_key()
    get_kubeconfig()
    helm_init()
    kubectx = environ['K8S_CLUSTER_CONTEXT']
    run_cmd(f'make apply kubectx={kubectx}', cwd='k8s')

def import_gpg_key():
    key_b64 = environ['HELM_GPG_KEY_B64']
    key = b64decode(key_b64)
    run_cmd('gpg --import', input=key.decode('utf-8'))

def get_kubeconfig():
    do_token = environ['DO_TOKEN_GET_KUBECONF']
    cluster_id = environ['DO_K8S_CLUSTER_ID']
    cmd = f'make get-kubeconf do_token={do_token} cluster_id={cluster_id}'
    run_cmd(cmd, cwd='k8s')
    environ["KUBECONFIG"] = path.abspath('kubeconfig.yml')

def helm_init():
    run_cmd('helm init --client-only')
    run_cmd('helm version')
    run_cmd('helmfile -v')
