import click
import shlex
from base64 import b64decode
from git import Repo
from os import environ, getcwd
from subprocess import run, CalledProcessError, STDOUT
from lib.config import logger

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

def get_git_hash(repo):
    return repo.git.rev_parse(f'HEAD', short=8)

def init_git():
    repo = Repo(getcwd())
    if not is_local():
        repo.config_writer().set_value('user', 'name', 'Verdun CI Bot').release()
        repo.config_writer().set_value('user', 'email', 'verdun-ci-bot@patrician.gold').release()
    return repo

def login_docker():
    docker_user = environ['DOCKER_USER']
    docker_password_b64 = environ['DOCKER_PASSWORD_B64']
    docker_password = b64decode(docker_password_b64)
    run_cmd(f'docker login --username={docker_user} --password-stdin', input=docker_password.decode('utf-8'))

def build_push_container(directory, image):
    if not is_local():
        login_docker()
    if is_dev():
        logger.info(f'Skipping building image {image}')
    else:
        run_cmd(f'docker build -t {image} {directory}')
        run_cmd(f'docker push {image}')
