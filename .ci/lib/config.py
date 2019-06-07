import coloredlogs
import logging
from ruamel.yaml import YAML

yaml = YAML(typ='safe')
yaml.default_flow_style = False
logger = logging.getLogger('circleci')
    
def init():
    coloredlogs.install(level='DEBUG')
