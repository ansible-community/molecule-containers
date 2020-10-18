"""Containers Driver Module."""

from __future__ import absolute_import

from molecule import logger

try:
    from molecule_docker.driver import Docker as DriverBackend
except ImportError:
    from molecule_podman.driver import Podman as DriverBackend

log = logger.get_logger(__name__)


class Container(DriverBackend):
    """
    Container Driver Class.

    This class aims to provide an agnostic container enginer implementation,
    which should allow users to consume whichever enginer they have available.
    """  # noqa

    def __init__(self, config=None):
        """Construct Container."""
        super().__init__(config)
        self._name = "containers"
