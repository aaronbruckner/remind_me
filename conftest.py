import pytest
from tests.given import Given

@pytest.fixture(scope="module")
def given() -> Given:
    return Given()