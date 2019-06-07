import click

from lib.util import changed_since_last_run_commit
from lib.frontend import frontend
from lib.k8s import k8s
from lib.config import init
from lib.ci import build_ci_image

@click.command()
@click.option('--local/--circleci', default=False)
@click.option('--dev/--prod', default=False)
@click.option('--run-k8s', is_flag=True)
@click.option('--run-frontend', is_flag=True)
def main(local, dev, run_k8s, run_frontend):
    if run_k8s:
        k8s()
    elif run_frontend:
        frontend()
        k8s()
    elif changed_since_last_run_commit(['.circleci']):
        build_ci_image()
    elif changed_since_last_run_commit(['frontend']):
        frontend()
        k8s()
    elif changed_since_last_run_commit(['k8s']):
        k8s()

if __name__ == '__main__':
    init()
    main()
