import pytest
from gendiff.gendiff import generate_diff


def test_plain():
    paths = [
        ('tests/fixtures/file1_recursive.json', 'tests/fixtures/file2_recursive.json', 'tests/fixtures/result_for_plain'),
        ('tests/fixtures/file1_recursive.yaml', 'tests/fixtures/file2_recursive.yaml', 'tests/fixtures/result_for_plain')
  ]
    for p in paths:
        res = generate_diff(p[0], p[1], 'plain')
        with open(p[2]) as file:
            answ = file.read()
            assert res == answ
