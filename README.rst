|Icon| |title|_
===============

.. |title| replace:: diffpy.sbm
.. _title: https://diffpy.github.io/diffpy.sbm

.. |Icon| image:: https://avatars.githubusercontent.com/diffpy
        :target: https://diffpy.github.io/diffpy.sbm
        :height: 100px

|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/diffpy/diffpy.sbm/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/diffpy/diffpy.sbm/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/diffpy/diffpy.sbm/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/diffpy/diffpy.sbm

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/diffpy.sbm
        :target: https://anaconda.org/conda-forge/diffpy.sbm

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/diffpy.sbm
        :target: https://pypi.org/project/diffpy.sbm/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/diffpy.sbm
        :target: https://pypi.org/project/diffpy.sbm/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/diffpy/diffpy.sbm/issues

Python package for computing a measure of how strongly a distortion breaks different symmetries

* LONGER DESCRIPTION HERE

For more information about the diffpy.sbm library, please consult our `online documentation <https://diffpy.github.io/diffpy.sbm>`_.

Citation
--------

If you use diffpy.sbm in a scientific publication, we would like you to cite this package as

        diffpy.sbm Package, https://github.com/diffpy/diffpy.sbm

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``diffpy.sbm_env`` ::

        conda create -n diffpy.sbm_env python=3
        conda activate diffpy.sbm_env

Then, to fully install ``diffpy.sbm`` in our active environment, run ::

        conda install diffpy.sbm

Another option is to use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``diffpy.sbm_env`` environment, type ::

        pip install diffpy.sbm

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/diffpy/diffpy.sbm/>`_. Once installed, ``cd`` into your ``diffpy.sbm`` directory
and run the following ::

        pip install .

Support and Contribute
----------------------

`Diffpy user group <https://groups.google.com/g/diffpy-users>`_ is the discussion forum for general questions and discussions about the use of diffpy.sbm. Please join the diffpy.sbm users community by joining the Google group. The diffpy.sbm project welcomes your expertise and enthusiasm!

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/diffpy/diffpy.sbm/issues>`_ and/or `submit a fix as a PR <https://github.com/diffpy/diffpy.sbm/pulls>`_. You can also post it to the `Diffpy user group <https://groups.google.com/g/diffpy-users>`_. 

Feel free to fork the project and contribute. To install diffpy.sbm
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contribuing, please read our `Code of Conduct <https://github.com/diffpy/diffpy.sbm/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on diffpy.sbm please visit the project `web-page <https://diffpy.github.io/>`_ or email Prof. Simon Billinge at sb2896@columbia.edu.
