**************************
Molecule Containers Plugin
**************************

.. image:: https://img.shields.io/pypi/v/molecule-containers.svg
   :target: https://pypi.org/project/molecule-containers
   :alt: PyPI Package

.. image:: https://github.com/ansible-community/molecule-containers/workflows/tox/badge.svg
   :target: https://github.com/ansible-community/molecule-containers/actions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/python/black
   :alt: Python Black Code Style

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: LICENSE
   :alt: Repository License

Molecule Containers is designed to be a **drop-in replacement for the existing
Docker and Podman drivers**, one that can transparently pick whichever backend
is found.

The driver preference is defined by
``MOLECULE_CONTAINERS_BACKEND=podman,docker`` and you can easily switch between
the two by setting this variable.

Keep in mind that if executable is not found, the driver will fallback to
first option in the list and likely fail later.

.. _get-involved:

Get Involved
============

* Join us in the ``#ansible-molecule`` channel on `Freenode`_.
* Join `discussions`_ forum.
* Join the community working group by checking the `wiki`_.
* Want to know about releases, subscribe to `ansible-announce list`_.
* For the full list of Ansible email Lists, IRC channels see the
  `communication page`_.

.. _`Freenode`: https://freenode.net
.. _`discussions`: https://github.com/ansible-community/molecule/discussions
.. _`ansible-announce list`: https://groups.google.com/group/ansible-announce
.. _`communication page`: https://docs.ansible.com/ansible/latest/community/communication.html
.. _`wiki`: https://github.com/ansible/community/wiki/molecule

.. _authors:

Authors
=======

* Sorin Sbarnea

.. _license:

License
=======

The `MIT`_ License.

.. _`MIT`: https://github.com/ansible-community/molecule/blob/master/LICENSE

The logo is licensed under the `Creative Commons NoDerivatives 4.0 License`_.

If you have some other use in mind, contact us.

.. _`Creative Commons NoDerivatives 4.0 License`: https://creativecommons.org/licenses/by-nd/4.0/
