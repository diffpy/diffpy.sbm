"""Unit tests for __version__.py
"""

import diffpy.sbm


def test_package_version():
    """Ensure the package version is defined and not set to the initial placeholder."""
    assert hasattr(diffpy.sbm, "__version__")
    assert diffpy.sbm.__version__ != "0.0.0"
