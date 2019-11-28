"""Test foo module."""

from foo import bar, foo


def test_foo():
    """Test foo function."""
    assert foo() == 'bar'
    assert foo() != 'foo'

def test_bar():
    """Test bar function."""
    assert bar() == 'foo'
    assert bar() != 'bar'
