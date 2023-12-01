import pytest

# Using Pytest Fixtures
@pytest.fixture
def one():
    return 1

def test_we_are(one):
    assert one == 1
