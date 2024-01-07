import os
from gendiff.parser import parse
from gendiff.formatters.formatter import get_format
from gendiff.diff_list import get_diff


def get_file_data(filepath):
    format = os.path.splitext(filepath)
    return parse(filepath, format[1])


def generate_diff(file1, file2, format='stylish'):
    f1 = get_file_data(file1)
    f2 = get_file_data(file2)
    diff_list = get_diff(f1, f2)
    answ = get_format(diff_list, format)
    return f"{answ}"
