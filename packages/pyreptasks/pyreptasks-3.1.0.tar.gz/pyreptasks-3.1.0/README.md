![PyPI](https://img.shields.io/pypi/v/pyreptasks)
![GitHub](https://img.shields.io/github/license/tsenovilla/pyreptasks)
[![CI](https://github.com/tsenovilla/pyreptasks/actions/workflows/ci.yaml/badge.svg)](https://github.com/tsenovilla/pyreptasks/actions/workflows/ci.yaml)
[![pre-commit](https://github.com/tsenovilla/pyreptasks/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/tsenovilla/pyreptasks/actions/workflows/pre-commit.yaml)
![Codecov](https://img.shields.io/codecov/c/gh/tsenovilla/pyreptasks)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/tsenovilla/pyreptasks)


Description
===========

This Python library provides the user with some tools useful to automate coding of repetitive tasks.

Installation and usage
======================

To install this package use : 

```bash
% pip install pyreptasks
```

If you want to install a specific version x.x.x, use:

```bash
% pip install pyreptasks==x.x.x
```

There is not need of other Python packages to correctly run `pyreptasks`.

To import all the classes and methods of the package in your Python projects: 

```python
from pyreptasks import *
```

You may find examples of usage in the folder `examples`.

Developing
==========

If you want to contribute, to ensure that you have all the needed dependencies installed in your local environment, install the requirements described in `requirement_files/develop_requirements.txt`. To do so, you can download the file or just copy it into a develop_requirements.txt file then do

```bash
% pip install -r develop_requirements.txt
```

This project uses `black` to format code. We support `pre-commit` to ensure this formatting has been run. If you have installed the requirements, you should have these packages already installed.

`Codecov` is set up for this project, so for any push or pull request you may check the code coverage report at https://app.codecov.io/gh/tsenovilla/pyreptasks. 

Testing
=======

This project uses `pytest` to run the tests defined in the folder `tests`. Tests ensure that future releases will not break the former functionality unexpectedly. If some functionality is updated, the tests must be updated accordingly. If a test fails, there are two possibilities: either the tests are not up to date (no problem, it is just an oversight, just make them be coherent with the new version) or something in the code has changed but it should not have been modified. It is up to the developper to determine the actual situation.

To run the tests locally, install the test requirements described in `requirement_files/tests_requirements.txt`. To do so, you can download the file or just copy it into a tests_requirements.txt then do

```bash
% pip install -r test_requirements.txt
```

To run all the tests, go to the repository where you have stored the folder `tests` and run:

```bash
% pytest
```

In the case that you would like to run only a specific test, select it individually, for example:

```bash
% pytest tests/test_switch.py
```

Versions log
============

Version 1.0.0
-------------

- New module `switch.py`: Contains the class Switch. Switch objects may be used to create friendly switch-case structures within a Switch object. This provide the programmer with the advantage of reusing the switch-case along the code if it is needed several times without copy/pasting it. As the object's configuration may be changed along the code, the same Switch object might be used for different switch-case structures sharing some part of their cases. Moreover, this tool might be used to define switch-case structures in Python versions 3.7, 3.8 and 3.9, where the match-case structure was not yet included into the language (version 3.10).

Version 2.0.0
-------------

- Update of module `switch.py`: From this version, integer_switch is not a parameter available for the class Switch   anymore. This parameter was used in a Switch object to indicate that the switch had to contain only integer keys. The parameter is deleted due to it was not actually useful. 

- Switch examples and tests updates to fit with the new version.

- Other changes: 
  - Adoption of the use of `setuptools_scm` (https://github.com/pypa/setuptools_scm/) package to manage version control instead of `versioneer`, used in the previous version. This also allows us to get rid of some configuration and version control files, in order to get a simpler package. 
  
  - Adoption of `pyproject.toml` introduced in the standard PEP 518. 

  - Creation of `release.yaml` to automate releases when a new tag is pushed to GitHub. 

Version 2.0.1
-------------

- Bug fix: The version 2.0.0 changed the folder's name containing the source code, named `pyreptasks`, to `src`, without creating a `pyreptasks` package inside. This change created a conflict when importing the package, as its name was not anymore `pyreptasks` but `src`. This new version solves that oversight by creating a Python package `pyreptasks` inside the `src` folder. 

- Deletion of the file `setup.py` as it is not needed anymore with the introduction of `pyproject.toml`

- The former file `requirements.txt` might have been misunderstood, as it does not contain the actual requirements to run `pyreptasks`, but the requirements to make correctly a git commitment. Due to up to this version there is not need of any other Python package to run `pyreptasks`, this file is now named `develop_requirements.txt`, and it is included in the new folder `requirement_files`, with the file containing the packages needed for testing (`tests_requirements.txt`). If `pyreptasks` needs another Python package to run in the future, the `requirements.txt` file would be created again to carry out its actual rol. 

- As `setup.py` is not available anymore, the workflow `release.yaml` have been updated accordingly.

Version 2.1.0
-------------

- New module `data_formatter.py`: This module introduces the class DataFormatter. An object created with this class allows to define fields that should respect certain format. There are several options to customize the format of each field. Then, the object is able to convert some data string into the format specified by the fields, as well as to ensure that the data respects the fields constraints, otherwise it will throw an exception. Everything is done in a few lines, enabling the developper to skip coding many data controls and format conversions.

Version 3.0.0
-------------

- Updates in the module `switch.py`: 

  - The Switch class does not need anymore a list of conditions and switch values. From this version, the switch configuration must be transmitted to the object via a dictionary containing the pairs {conditions : actions}. This makes easier to configure the switch-case structure.

  - Switch attributes cannot be accesed in a direct way from this version. This update protects the programmer against the possibility of changing the values by error, and so getting an unexpected execution of the Switch. New methods have been included allowing the programmer to modify the attributes.

- The workflow `ci.yaml` has been updated to run the tests in every Python version from 3.7, to ensure the library is compatible with all of them.

- Updates in the module `data_formatter.py`: As this module uses a Switch object, the code has been updated to fit with the new version.

- Tests and examples have been also updated to fit with the new version.

Version 3.1.0
-------------

- Updates in the module `data_formatter.py`:

  - The attribute `fields` cannot be accesed in a direct way from this version. This update protects the programmer against the possibility of changing the values by error, and so getting an unexpected execution of the DataFormatter object. A new method `field_format` has been added to show the format of a specific field introduced as input.

  - The method `add_field` has a new argument called `required`. As its name suggests, this field tells the formatter that the field must contain some characters to be valid.

  - Bug fixs: 
    1. The arguments `length_range` and `value_range` of the `add_field` method could be not well-formed in previous versions and the method did not check them correctly. In particular, the method checked that they were lists of length 0 or 2, but did not check their content. From this version, the list must be formed of actual range bonds. 

    2. Fields did not accept empty strings even if the length range specified that length zero is accepted. This was produced because native methods such isalpha or int() does not support empty strings. 

- Tests and examples have been also updated to fit with the new version.


Workflows
=========

- CI (Continuous Integration): This workflow runs the test files contained in `tests` using `pytest` in each Python version from 3.7, ensuring that the library might be used in all of them. It also runs code coverage to ensure the whole code is being used. 

- Pre-commit: This workflow ensures that all Python files respect PEP 8 formatting, via `black`.

- Build distribution: This workflow ensures that each time a push/pull request is made, the project is in a packageable state. Furthermore, if a tag is pushed, the workflow publishes the package on PyPI and Conda.


Other
=====

Author: Tomás Senovilla Polo

Email : tspscgs@gmail.com

License: pyreptasks is available under the MIT license. See `LICENSE.txt` for more information.

If you have in mind some functionality deserving to be included in `pyreptasks`, let me know it! I will be happy to include it in future releases :smile: 