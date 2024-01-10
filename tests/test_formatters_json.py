import pytest
from gendiff.gendiff import generate_diff


def test_json():
    paths = [
      ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/result_for_json.json'),
      ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'tests/fixtures/result_for_json.json')
    ]
    for p in paths:
        res = generate_diff(p[0], p[1], 'json')
        with open(p[2]) as file:
            answ = file.read()
            assert res == answ
