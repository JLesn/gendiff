import os
from gendiff.parser import parse


def to_string(diff_list):
    splited = diff_list.rstrip().split('\n')
    res = sorted(splited, key=lambda x: x[3])
    return '\n'.join(res).lower()


def generate_diff(filepath1, filepath2):
    f1 = get_file_data(filepath1)
    f2 = get_file_data(filepath2)
    diff_list = ''
    f1_unique_keys = f1.keys() - f2.keys()
    f2_unique_keys = f2.keys() - f1.keys()
    common_keys = f1.keys() & f2.keys()
    for key in common_keys:
        if f1[key] != f2[key]:
            diff_list += f' - {key}: {f1[key]}\n'
            diff_list += f' + {key}: {f2[key]}\n'
        else:
            diff_list += f'   {key}: {f1[key]} \n'
    for key in f1_unique_keys:
        diff_list += f' - {key}: {f1[key]} \n'
    for key in f2_unique_keys:
        diff_list += f' + {key}: {f2[key]} \n'
    answ = to_string(diff_list)
    return '{ \n' + answ + ' \n} \n'


def get_file_data(filepath):
    format = os.path.splitext(filepath)
    return parse(filepath, format[1])
