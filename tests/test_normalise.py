from nutriunit.normalise import per_100g, per_serving, per_mj

def test_per_100g():
    assert per_100g(12, 50) == 24

def test_per_serving():
    assert per_serving(12, 150) == 12 / 150

def test_per_mj():
    assert per_mj(12, 500) == 24
