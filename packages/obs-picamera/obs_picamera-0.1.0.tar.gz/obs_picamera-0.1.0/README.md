# obs-picamera

[![PyPI](https://img.shields.io/pypi/v/obs-picamera?style=flat-square)](https://pypi.python.org/pypi/obs-picamera/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/obs-picamera?style=flat-square)](https://pypi.python.org/pypi/obs-picamera/)
[![PyPI - License](https://img.shields.io/pypi/l/obs-picamera?style=flat-square)](https://pypi.python.org/pypi/obs-picamera/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://gluap.github.io/obs-picamera](https://gluap.github.io/obs-picamera)

**Source Code**: [https://github.com/gluap/obs-picamera](https://github.com/gluap/obs-picamera)

**PyPI**: [https://pypi.org/project/obs-picamera/](https://pypi.org/project/obs-picamera/)

---

A python module to record video of overtaking events to allow vehicle type identification for OpenBikeSensor overtaking events.

## Building the device

This software should work with a Pi Zero W or Pi Zero 2 with raspberry pi camera independently from the case it's mounted in.

The idea is to run this on a raspberry pi zero case which can be somehow mounted on the bicycle. An example case for such a mounting with a list of components used can be found [here](https://github.com/gluap/OpenBikeSensor3dPrintableCase/tree/camlid/src/Attachments), compiled STL files to match it are available [with logos](https://github.com/gluap/OpenBikeSensor3dPrintableCase/tree/camlid/export/logo/OpenBikeSensor) [and without](https://github.com/gluap/OpenBikeSensor3dPrintableCase/tree/camlid/export/Attachments)

## Installation of ``obs-picamera``

The software is meant to run on a raspberry pi zero. I suggest installing it with Raspberry Pi os. As prerequisites the following packages are required:

```commandline
sudo apt install python-picamera2 python3-pip
```

The package can then be installed as usual via pip.

```sh
pip install --user obs-picamera # add --upgrade if you want to upgrade
```

## Using ``obs-picamera``

You can run the program by calling (``pip install --user`` has installed the binary in your ``~/.local/bin/``)
```commandline
obs_picamera
```

When it finds an OpenBikeSensor via bluetooth enabled, it will pair with it and whenever it receives an overtaking event
- Events for one OpenBikeSensor Track are stored in a directory with the track-id as the directory name.
- For each event a short ``h264`` video file is saved, the filename matching the system time of the OpenBikeSensor.
- Next to the video file a ``.json`` file with the Data from the overtaking event is placed. Its content is self-explanatory. The distance already has the handlebar width deducted.

I suggest starting obs_picamera automatically at boot - for instance via crontab entry and switching the pi on while still in the home WIFI (which will enable it to pick up a sensible time). Or one may create a phone wifi for it to pick up the time and date



## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/gluap/obs-picamera/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/gluap/obs-picamera/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/gluap/obs-picamera/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

---

This project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
