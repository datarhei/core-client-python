import pytest

pytestmark = pytest.mark.integration

# (key, value, expected python type) for the round-trip checks.
CASES = [
    ("1", '"1"', str),
    ("2", 1, int),
    ("3", [1], list),
    ("4", {"1": 1}, dict),
]


@pytest.mark.parametrize("key,value,expected", CASES, ids=[c[0] for c in CASES])
def test_metadata_put_get_roundtrip(admin_client, key, value, expected):
    assert isinstance(admin_client.v3_metadata_put(key=key, data=value), expected)
    assert isinstance(admin_client.v3_metadata_get(key=key), expected)
