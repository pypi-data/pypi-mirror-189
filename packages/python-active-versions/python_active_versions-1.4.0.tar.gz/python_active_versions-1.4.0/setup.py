# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_active_versions', 'python_active_versions.cli_tools', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['cloup>=2.0.0,<3.0.0',
 'requests-html>=0.10.0,<0.11.0',
 'requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['python-active-versions = '
                     'python_active_versions.cli_tools.cli:get_python_versions']}

setup_kwargs = {
    'name': 'python-active-versions',
    'version': '1.4.0',
    'description': 'Gather active python versions.',
    'long_description': "# python active versions\n\n\n[![pypi](https://img.shields.io/pypi/v/python-active-versions.svg)](https://pypi.org/project/python-active-versions/)\n[![python](https://img.shields.io/pypi/pyversions/python-active-versions.svg)](https://pypi.org/project/python-active-versions/)\n[![Build Status](https://github.com/gpongelli/python-active-versions/actions/workflows/dev.yml/badge.svg)](https://github.com/gpongelli/python-active-versions/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/gpongelli/python-active-versions/branch/main/graphs/badge.svg)](https://codecov.io/github/gpongelli/python-active-versions)\n\n\n\nGather active python versions and, optionally, also docker images.\n\n\n* Documentation: <https://gpongelli.github.io/python-active-versions>\n* GitHub: <https://github.com/gpongelli/python-active-versions>\n* PyPI: <https://pypi.org/project/python-active-versions/>\n* Free software: MIT\n\n\n## Features\n\n* Scrape official python website to get active versions\n* Scrape dockerhub website to add optional python's available images\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [gpongelli/cookiecutter-pypackage](https://github.com/gpongelli/cookiecutter-pypackage) project template.\n",
    'author': 'Gabriele Pongelli',
    'author_email': 'gabriele.pongelli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gpongelli/python-active-versions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0',
}


setup(**setup_kwargs)
