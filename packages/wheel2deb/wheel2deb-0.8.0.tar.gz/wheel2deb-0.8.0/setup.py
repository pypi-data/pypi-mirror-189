# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wheel2deb']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3,<4',
 'PyYAML>=6,<7',
 'attrs>=20.1',
 'colorama',
 'dirsync',
 'packaging',
 'pkginfo',
 'rich',
 'typer>=0.6.1',
 'wheel']

extras_require = \
{'pyinstaller': ['pyinstaller==5.4.1']}

entry_points = \
{'console_scripts': ['wheel2deb = wheel2deb.cli:main']}

setup_kwargs = {
    'name': 'wheel2deb',
    'version': '0.8.0',
    'description': 'Python wheel to debian package converter',
    'long_description': '## wheel2deb\n\n![cicd](https://github.com/upciti/wheel2deb/actions/workflows/cicd.yml/badge.svg)\n[![codecov](https://codecov.io/gh/upciti/wheel2deb/branch/main/graph/badge.svg)](https://codecov.io/gh/upciti/wheel2deb)\n[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![PyPI version shields.io](https://img.shields.io/pypi/v/wheel2deb.svg)](https://pypi.python.org/pypi/wheel2deb/)\n[![Downloads](https://static.pepy.tech/personalized-badge/wheel2deb?period=total&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/wheel2deb)\n[![WakeMeOps](https://docs.wakemeops.com/badges/wheel2deb.svg)](https://docs.wakemeops.com/packages/wheel2deb)\n\n`wheel2deb` is a python wheel to debian package converter. It takes a list of wheels as input and produces a list of debian binary CPython packages (those prefixed with python- or python3-).\n\n[![asciicast](https://asciinema.org/a/249779.svg)](https://asciinema.org/a/249779)\n\n## Quick Example\n\nThe following shows how to convert numpy and pytest, along with their dependencies into a list of debian packages:\n\n```sh\n# Download (and build if needed) pytest, numpy and their requirements\npip3 wheel pytest numpy\n# Convert all wheels to debian source packages, build them with dpkg-buildpackage\nwheel2deb\nls -l output/*.deb\n# Install generated packages\ndpkg -i output/*.deb\n# Run pytest on numpy\npython3 -c "import numpy; numpy.test()"\n```\n\n## Project scope\n\n- Python 2.7 and 3\n- CPython only for now\n- support for non pure python wheels\n- support debian architectures all, armhf, amd64, i686\n- tested on jessie, stretch, buster so far, ubuntu should also work\n\n## Requirements\n\n`wheel2deb` uses `apt-cache` to search for debian packages, `dpkg-shlibdeps` to calculate shared library dependencies and `apt-file` to search packages providing shared library dependencies. `wheel2deb build` requires the usual tools to build a debian package:\n\n```sh\napt update\napt install apt-file dpkg-dev fakeroot build-essential devscripts debhelper\napt-file update\n```\n\nIf you want to cross build packages for ARM, you will also need to install `binutils-arm-linux-gnueabihf`.\n\nConverting pure python wheels, don\'t actually requires apt-file and dpkg-dev.\n\nKeep in mind that you should only convert wheels that have been built for your distribution and architecture. wheel2deb will not warn you about ABI compatibility issues.\n\n## Installation\n\n### From the release page\n\n`wheel2deb` is packaged as a single binary application that you can download from the release page. Using those releases will spare you the hassle of building Python 3.10 on old Debian based distributions.\n\n### With [wakemeops](https://docs.wakemeops.com)\n\n```shell\nsudo apt-get install wheel2deb\n```\n\n### With docker\n\nWe currently do not build docker images with `wheel2deb` pre-installed. You can use wakemeops docker images to quickly play with `wheel2deb` on a different distribution than your host.\n\n```shell\ndocker run -ti wakemeops/debian:buster\n```\n\nAnd in the container run:\n\n```\ninstall_packages wheel2deb\n```\n\n### With [pipx](https://github.com/pipxproject/pipx)\n\n`wheel2deb` is available from [pypi](https://pypi.org/project/wheel2deb/):\n\n```shell\npipx install wheel2deb\n```\n\n## Features\n\n- guess debian package names from wheel names and search for them in the cache\n- search packages providing shared library dependencies for wheels with native code\n- handle entrypoints and scripts (those will be installed in /usr/bin with a proper shebang)\n- try to locate licence files and to generate a debian/copyright file\n\n## Usage\n\nUse `wheel2deb convert --help` and `wheel2deb build --help` to check all supported options.\n\n## Development\n\nYou will need [poetry](https://python-poetry.org/), and probably [pyenv](https://github.com/pyenv/pyenv) if you don\'t have python 3.10 on your host.\n\n```shell\npoetry install\n```\n\nTo run wheel2deb test suite run:\n\n```shell\npoetry run task check\n```\n\nTo build a python wheel:\n\n```shell\npoetry run poetry build\n```\n\n## Bugs/Requests\n\nPlease use the [GitHub issue tracker](https://github.com/upciti/wheel2deb/issues) to submit bugs or request features.\n\n## License\n\nCopyright Parkoview SA 2019-2023.\n\nDistributed under the terms of the [MIT](https://github.com/upciti/wheel2deb/blob/master/LICENSE) license, wheel2deb is free and open source software.\n',
    'author': 'Upciti',
    'author_email': 'support@upciti.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/upciti/wheel2deb',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
