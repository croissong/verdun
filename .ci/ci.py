from os import environ, path
import click
from base64 import b64decode
from lib.config import init
from lib.util import is_local, run_cmd

init()

@click.command()
@click.option('--local/--ci', default=False)
@click.option('--dev/--prod', default=False)
def ci(local, dev):
    if not is_local():
        import_gpg_key()
        get_kubeconfig()
        helm_init()
        kubectx = environ['K8S_CLUSTER_CONTEXT']
    else:
        kubectx = environ['KUBECONTEXT']
    run_cmd(f'make apply kubectx={kubectx}', cwd='k8s', check=False)

def import_gpg_key():
    key_b64 = environ['HELM_GPG_KEY_B64']
    key = b64decode(key_b64)
    with open('gpg_key.txt', 'wb') as w:
        w.write(key)
    run_cmd('gpg --import gpg_key.txt')

def get_kubeconfig():
    do_token = environ['DO_TOKEN_GET_KUBECONF']
    cluster_id = environ['DO_K8S_CLUSTER_ID']
    cmd = f'make get-kubeconf do_token={do_token} cluster_id={cluster_id}'
    run_cmd(cmd, cwd='k8s')
    environ["KUBECONFIG"] = path.abspath('kubeconfig.yml')

def helm_init():
    run_cmd('helm init --client-only')
    run_cmd('helmfile -v')

if __name__ == '__main__':
    ci()
