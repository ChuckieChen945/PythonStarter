"""Test PythonStarter."""

import pythonstarter


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(pythonstarter.__name__, str)
