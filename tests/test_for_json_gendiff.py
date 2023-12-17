from gendiff.gendiff import generate_diff
import pytest


def test_generate_diff():
    with open('tests/fixtures/result_for_json') as file:
        answ = file.read()
    res = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert res == answ
