import json
import yaml


def parse(path, format):
    if format == '.json':
        return json.load(open(path))
    if format == '.yml' or format == '.yaml':
        return yaml.safe_load(open(path))
