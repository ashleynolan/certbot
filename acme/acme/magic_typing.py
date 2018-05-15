"""Shim class to not have to depend on typing module in prod."""
import sys

class TypingClass(object):
    """Ignore import errors by getting anything"""
    def __getattr__(self, name):
        return None

try:
    # mypy doesn't respect modifying sys.modules
    from typing import * # pylint: disable=wildcard-import, unused-wildcard-import
    from typing import IO  # pylint: disable=unused-import
except ImportError:
    sys.modules[__name__] = TypingClass()
