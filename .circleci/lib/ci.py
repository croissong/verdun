from lib.util import build_push_container

def build_ci_image():
    image = f'croissong/verdun-ci:latest'
    build_push_container('.circleci', image)
