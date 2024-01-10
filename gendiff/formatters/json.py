import json

def json_formatter(diff_list):
    return json.dumps(diff_list, indent=4)
