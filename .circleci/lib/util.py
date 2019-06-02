import click
import os
import sys
import shlex
from subprocess import run
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
        result = os.popen(cmd).read()
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
    return os.getenv('CIRCLE_SHA1', '')

def is_local() -> bool:
    return click.get_current_context().params['local']

def is_dev() -> bool:
    return click.get_current_context().params['dev']

def run_cmd(cmd, check=True, input=None, cwd=None):
    p = run(shlex.split(cmd), check=check, input=input, universal_newlines=True, cwd=cwd)
    return p.stdout
