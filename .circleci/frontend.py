import click
import shlex
import coloredlogs
import logging
from git import Repo
from ruamel.yaml import YAML
from subprocess import run
from os import environ, getcwd
from base64 import b64decode

@click.command()
@click.option('--local/--circleci', default=False)
@click.option('--dev/--prod', default=False)
def main(local, dev):
    repo = init_git(local)
    tag = repo.git.rev_parse('HEAD', short=8)
    build_push_container(tag, local, dev)
    update_images(tag)
    git_push(repo, tag, local, dev)

def build_push_container(tag, local, dev):
    if not local:
        login_docker()
    image = f'croissong/verdun-frontend:{tag}'
    if dev:
        print(f'Skipping building image {image}')
    else:
        run_cmd(f'docker build -t {image} frontend')
        run_cmd(f'docker push {image}')

def update_images(tag):
    with open('k8s/values/images.yml', 'r+', encoding='utf-8') as f:
        images = yaml.load(f)
        images['verdun']['frontend']['tag'] = tag
        f.seek(0)
        f.truncate()
        yaml.dump(images, f)

def git_push(repo, tag, local, dev):
    if not repo.is_dirty():
        return
    if not local:
        branch = environ['CIRCLE_BRANCH']
        repo.git.checkout(branch)
        repo.git.pull('origin', branch)
        logger.info(f'checked out and pulled branch {branch}')
    else:
        branch = repo.active_branch

    repo.git.add('k8s')
    repo.git.commit('-m', 'Bump verdun-frontend -> {tag}[ci skip]')
    if not dev:
        repo.git.push('origin', branch)

def init_git(local):
    repo = Repo(getcwd())
    if not local:
        repo.config_writer().set_value("user", "name", "Verdun CI Bot").release()
        repo.config_writer().set_value("user", "email", "verdun-ci-bot@patrician.gold").release()
    return repo

def login_docker():
    docker_user = environ['DOCKER_USER']
    docker_password_b64 = environ['DOCKER_PASSWORD_B64']
    docker_password = b64decode(docker_password_b64)
    print(docker_password)
    run_cmd(f"docker login --username={docker_user} --password-stdin", input=docker_password.decode("utf-8"))

def run_cmd(cmd, check=True, input=None):
    p = run(shlex.split(cmd), check=check, input=input, universal_newlines=True)
    return p.stdout

def global_config():
    global yaml
    yaml = YAML(typ='safe')
    yaml.default_flow_style = False
    global logger
    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG')

if __name__ == "__main__":
    global_config()
    main()
