from hello import add

def test_add():
    assert add(1, 2) == 3
    assert add(3, 4) == 7
    assert add(5, 6) == 11