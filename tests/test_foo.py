"""Test foo module."""

from foo import foo


def test_foo():
    """Test foo function."""
    assert foo() == 'foo'
    assert foo() != 'bar'
