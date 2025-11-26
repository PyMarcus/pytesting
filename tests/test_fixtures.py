import pytest


@pytest.fixture
def sample_list():
    return [1, 0]


def test_sum_list(sample_list):
    assert sum(sample_list) == 1


def test_list_length(sample_list):
    assert len(sample_list) == 2
