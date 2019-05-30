import yaml
from subprocess import check_output
from os import environ
from base64 import b64decode

docker_user = environ['DOCKER_USER']
docker_password_b64 = environ['DOCKER_PASSWORD_B64']

def main():
    init_git()
    tag = check_output('git rev-parse --short HEAD'.split(), universal_newlines=True).split()[0]
    build_push_container(tag)
    update_helmfile(tag)

def build_push_container(tag):
    docker_password = b64decode(docker_password_b64)
    check_output(f"docker login --username={docker_user} --password-stdin".split(), input=docker_password)
    image = f'croissong/verdun-frontend:{tag}'
    check_output(f'docker build -t {image} frontend'.split())
    check_output(f'docker push {image}'.split())

def update_helmfile(tag):
    helmfile = yaml.load('k8s/helmfile.yaml')

def init_git():
    check_output('git config user.email "jan.moeller0@gmail.com"'.split())
    check_output('git config user.name "Jan Möller""'.split())

if __name__ == "__main__":
    main()
