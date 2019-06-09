import click
import shlex
from subprocess import run, CalledProcessError, STDOUT

def is_local() -> bool:
    return click.get_current_context().params['local']

def is_dev() -> bool:
    return click.get_current_context().params['dev']

def run_cmd(cmd, check=True, input=None, cwd=None):
    try:
        p = run(shlex.split(cmd), stderr=STDOUT, check=check, input=input, universal_newlines=True, cwd=cwd)
        return p.stdout
    except CalledProcessError as e:
        print(e.output)
        raise e
