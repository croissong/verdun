import click
import shlex
from base64 import b64decode
from git import Repo
from os import environ, getcwd, popen
from subprocess import run, CalledProcessError, STDOUT
from lib.config import logger

def changed_since_last_run_commit(dirs: list) -> bool:
    if is_local():
        return True
    compare_url = git_compare_url()
    if not compare_url:
        logger.info("CIRCLE_COMPARE_URL missing")
        return True
    else:
        logger.info(f'Compare url: {compare_url}')
        # We redirect stderr to stdout. If there is an error (e.g. in the first pipeline or some other edge cases), we regard everything as changed
        last_run_commit = get_last_run_commit()
        current_run_commit = get_current_run_commit()
        directories = ' '.join(dirs)
        cmd = f'git diff {last_run_commit} {current_run_commit} {directories} 2>&1'
        logger.info(cmd)
        result = popen(cmd).read()
        changed = not not result
        logger.info(f'{result} - changed: {changed}')
        return changed

def git_compare_url() -> str:
    with open('workspace/CIRCLE_COMPARE_URL.txt', 'r') as file:
        CIRCLE_COMPARE_URL = file.read()
    return CIRCLE_COMPARE_URL


# https://discuss.gradle.org/t/build-scan-plugin-1-10-3-issue-when-using-a-url-with-a-caret/24965
def get_last_run_commit() -> str:
    return git_compare_url().split('/compare/')[1].split('...')[0].replace('^', '')


def get_current_run_commit() -> str:
    return environ['CIRCLE_SHA1']

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
