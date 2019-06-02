import click

from lib.util import changed_since_last_run_commit
from lib.frontend import frontend
from lib.k8s import k8s
from lib.config import init


@click.command()
@click.option('--local/--circleci', default=False)
@click.option('--dev/--prod', default=False)
def main(local, dev):
    if changed_since_last_run_commit('frontend'):
        frontend()
        k8s()
    elif changed_since_last_run_commit('k8s'):
        k8s()

if __name__ == '__main__':
    init()
    main()
