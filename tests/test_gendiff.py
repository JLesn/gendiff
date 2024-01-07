from gendiff.gendiff import generate_diff
import pytest


paths = [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json', 'tests/fixtures/result_for_json'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'json', 'tests/fixtures/result_for_json'),
    ('tests/fixtures/file1_recursive.json', 'tests/fixtures/file2_recursive.json', 'stylish', 'tests/fixtures/result_for_recursive'),
    ('tests/fixtures/file1_recursive.yaml', 'tests/fixtures/file2_recursive.yaml', 'stylish', 'tests/fixtures/result_for_recursive'),
    ('tests/fixtures/file1_recursive.json', 'tests/fixtures/file2_recursive.json', 'plain', 'tests/fixtures/result_for_plain'),
    ('tests/fixtures/file1_recursive.yaml', 'tests/fixtures/file2_recursive.yaml', 'plain', 'tests/fixtures/result_for_plain')
]

def test_gendiff():
    for path in paths:
        with open(path[3]) as file:
            answ = file.read()
        res = generate_diff(path[0], path[1], path[2])
        assert res == answ
