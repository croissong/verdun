from subprocess import check_output

def main():
    init_git()
    tag = check_output('git rev-parse --short HEAD'.split(), universal_newlines=True).split()[0]
    build_push_container(tag)

def build_push_container(tag):
    image = f'cloud.canister.io:5000/croissong/verdun:{tag}'
    check_output(f'docker build -t {image}'.split())
    check_output(f'docker pull {image}'.split())

def init_git():
    check_output('git config user.email "jan.moeller0@gmail.com"'.split())
    check_output('git config user.name "Jan Möller""'.split())

if __name__ == "__main__":
    main()
