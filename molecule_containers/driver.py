"""Containers Driver Module."""
from __future__ import absolute_import

import inspect
import os
import shutil

from molecule import logger

_logger = logger.get_logger(__name__)

# Temporary logic to determine which backend driver should be loaded.
# podman is used as fallback default.
driver = os.environ.get("MOLECULE_CONTAINERS_BACKEND", "")
if not driver:
    if "DOCKER_HOST" in os.environ:
        driver = "docker"
    elif "CONTAINER_HOST" in os.environ:
        driver = "podman"
    else:
        if shutil.which("docker"):
            driver = "docker"
        else:
            driver = "podman"

# Logic for picking backend is subject to change.
if driver == "docker":
    from molecule_docker.driver import Docker as DriverBackend
elif driver == "podman":
    from molecule_podman.driver import Podman as DriverBackend
else:
    raise NotImplementedError("Driver %s is not supported." % driver)
_logger.debug("Containers driver will use %s backend", driver)


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
        # Assure that _path points to the driver we would be using, or
        # molecule will fail to find the embedded playbooks.
        self._path = os.path.abspath(os.path.dirname(inspect.getfile(DriverBackend)))
