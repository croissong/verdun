from os import environ
from lib.util import is_dev, is_local, run_cmd, get_git_hash, init_git, build_push_container
from lib.config import logger, yaml

def frontend():
    repo = init_git()
    tag = get_git_hash(repo)
    run_cmd('yarn install', cwd='frontend')
    run_cmd('yarn build', cwd='frontend')
    image = f'croissong/verdun-frontend:{tag}'
    build_push_container('frontend', image)
    update_images(tag)
    git_push(repo, tag)

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


