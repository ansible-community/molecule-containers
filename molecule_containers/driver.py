"""Containers Driver Module."""

from __future__ import absolute_import


from molecule import logger

try:
    from molecule.driver.docker import Docker as DriverBackend
except ImportError:
    from molecule.driver.podman import Podman as DriverBackend

log = logger.get_logger(__name__)


class Container(DriverBackend):
    """
    Container Driver Class.

    This class aims to provide an agnostic container enginer implementation,
    which should allow users to consume whichever enginer they have available.
    """  # noqa

    def __init__(self, config=None):
        """Construct Container."""
        super(DriverBackend, self).__init__(config)
        self._name = "containers"
