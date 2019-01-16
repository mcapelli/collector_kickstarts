========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/collector_kickstarts/badge/?style=flat
    :target: https://readthedocs.org/projects/collector_kickstarts
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/mcapelli/collector_kickstarts.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/mcapelli/collector_kickstarts

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/mcapelli/collector_kickstarts?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/mcapelli/collector_kickstarts

.. |requires| image:: https://requires.io/github/mcapelli/collector_kickstarts/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/mcapelli/collector_kickstarts/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/mcapelli/collector_kickstarts/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/mcapelli/collector_kickstarts

.. |version| image:: https://img.shields.io/pypi/v/collector-kickstarts.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/collector-kickstarts

.. |commits-since| image:: https://img.shields.io/github/commits-since/mcapelli/collector_kickstarts/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mcapelli/collector_kickstarts/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/collector-kickstarts.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/collector-kickstarts

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/collector-kickstarts.svg
    :alt: Supported versions
    :target: https://pypi.org/project/collector-kickstarts

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/collector-kickstarts.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/collector-kickstarts


.. end-badges

kickstat templates

* Free software: BSD 2-Clause License

Installation
============

::

    pip install collector-kickstarts

Documentation
=============


https://collector_kickstarts.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
