"""Test foo module."""

from foo import bar, foo


def test_foo():
    """Test foo function."""
    assert foo() == 'foo'
    assert foo() != 'bar'

def test_bar():
    """Test bar function."""
    assert bar() == 'bar'
    assert bar() != 'foo'
