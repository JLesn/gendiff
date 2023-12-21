from gendiff.gendiff import generate_diff
import pytest


def test_generate_diff():
    with open('tests/fixtures/result_for_yaml') as file:
        answ = file.read()
    res = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    assert res == answ
