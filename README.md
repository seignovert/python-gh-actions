Test python package with Github actions
=======================================

[![Github Actions](https://github.com/seignovert/python-gh-actions/workflows/Github%20Actions/badge.svg)](https://github.com/seignovert/python-gh-actions/actions?query=workflow%3AGithub%20Actions)

See [`.github/workflows/actions.yml`](.github/workflows/actions.yml)

## On push or pull request

Continuous Integration (CI):
* run `flake8`
* run `pylint`
* run `pytest` with python matrix `[3.6, 3.7, 3.8]`

Triggered only when a `**.py` file is included in the event.

## On tag

Continuous Delivery (CD):
* run CI first then on success
* deploy to `PyPI`.
* add to `Github releases`.

Triggered only when a `tag` is present.

## Deploy setup

Create an `API TOKEN` in PyPI (PyPI > Account settings > API tokens > Add API token) and
add the value as `PYPI_TOKEN` to the repository secrets (Github repo > Settings > Secrets > Add a new secret).

> Optional: Set/edit `PYPI_REPO` env variable in [`.github/workflows/actions.yml`](.github/workflows/actions.yml)
> to change deploy PyPI repository URL (`https://test.pypi.org/legacy/` by default).