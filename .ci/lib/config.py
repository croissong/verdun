import coloredlogs
import logging

logger = logging.getLogger('circleci')

def init():
    coloredlogs.install(level='DEBUG')
