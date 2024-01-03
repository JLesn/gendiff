import argparse


def args_for_script():
    parser = argparse.ArgumentParser(
        prog='gendiff', description='Generate differences')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
