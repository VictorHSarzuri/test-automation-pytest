import pytest

# pytes fixture
@pytest.fixture
def important_value():
    important = True
    return important