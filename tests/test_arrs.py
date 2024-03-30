from utils import arrs
from utils import add_f
import pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], None, 3) == [1, 2, 3]

@pytest.fixture()
def get():
    return {1: 'one', 2: 'two', 3: 'three'}


def test_get_val(get):
    assert add_f.get_val(get, 2, 'git') == 'two'
    assert add_f.get_val(get, 4, 'git') == 'git'
    assert add_f.get_val(get, 4, 'another') == 'another'
    assert add_f.get_val(get, 2, None) == 'two'