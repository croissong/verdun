from subprocess import check_output, run

def main():
    init_git()
    delete_old_tags()
    tag = check_output('git rev-parse --short HEAD'.split())
    check_output(f'git tag {tag}'.split())
    check_output(f'git push origin {tag}'.split())

def delete_old_tags():
    run('git push origin --delete $(git tag -l)'.split(), shell=True)
    run('git tag -d $(git tag -l)'.split(), shell=True)

def init_git():
    check_output('git config user.email "jan.moeller0@gmail.com"'.split())
    check_output('git config user.name "Jan Möller""'.split())

if __name__ == "__main__":
    main()
