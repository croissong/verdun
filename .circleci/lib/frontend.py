from git import Repo
from os import environ, getcwd
from base64 import b64decode
from lib.util import is_dev, is_local, run_cmd
from lib.config import logger, yaml

def frontend():
    repo = init_git()
    tag = repo.git.rev_parse('HEAD', short=8)
    run_cmd('yarn install')
    run_cmd('yarn build')
    build_push_container(tag)
    update_images(tag)
    git_push(repo, tag)

def build_push_container(tag):
    if not is_local():
        login_docker()
    image = f'croissong/verdun-frontend:{tag}'
    if is_dev():
        logger.info(f'Skipping building image {image}')
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

def git_push(repo, tag):
    if not repo.is_dirty():
        return
    if not is_local():
        branch = environ['CIRCLE_BRANCH']
        repo.git.checkout(branch)
        repo.git.pull('origin', branch)
        logger.info(f'checked out and pulled branch {branch}')
    else:
        branch = repo.active_branch

    repo.git.add('k8s')
    repo.git.commit('-m', f'Bump verdun-frontend -> {tag} [ci skip]')
    if not is_dev():
        repo.git.push('origin', branch)

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

