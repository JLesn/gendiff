#!/usr/bin/env python
from gendiff.gendiff import generate_diff
from gendiff.argparse import args_for_script


def main():
    file1, file2, format = args_for_script()
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
