Test python package with Github actions
=======================================

[![Tests and Linter](https://github.com/seignovert/python-gh-actions/workflows/Tests%20and%20Linter/badge.svg)](https://github.com/seignovert/python-gh-actions/actions?query=workflow%3ATests%20and%20Linter)
[![Deploy to PyPI](https://github.com/seignovert/python-gh-actions/workflows/Deploy%20to%20PyPI/badge.svg)](https://github.com/seignovert/python-gh-actions/actions?query=workflow%3ADeploy%20to%20PyPI)

* See [.github/workflows/push-pr-py.yml](.github/workflows/push-pr-py.yml) for `push` and `pull request` CI using `flake8`, `pylint` and `pytest` (3.6 / 3.7 / 3.8) when `**.py` is committed.
* See [.github/workflows/tag.yml](.github/workflows/tag.yml) for `tag` CD to deploy to `PyPI` and `Github releases`.