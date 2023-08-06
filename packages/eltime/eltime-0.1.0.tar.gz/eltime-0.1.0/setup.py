# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['eltime']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.0']

entry_points = \
{'console_scripts': ['eltime = eltime:main']}

setup_kwargs = {
    'name': 'eltime',
    'version': '0.1.0',
    'description': 'The simplest possible time tracker',
    'long_description': 'The simplest possible time tracker:\n\n- press Enter on window or mouse click Play button to start session\n\n- press Enter or mouse click Stop button to end session\n\nOptionally task description may be entered. Autocompletion will make suggestions from previous task.\n\nTo see stats for the last two days, press Ctrl-H\n\n---\nNote 1:\n\nIntentionally time duration is combined all over the each single hour for each task name, then total amount rounded up to 10min.\n\nE.g.:\n- three sessions by 1 min each calculates as 10min\n- two sessions by 7 min each and one 1min calculates as 20min\n\n---\nNote 2: \n\nHour activity ended is one that counts.\n\nE.g.:\n\n- session started 17:57 ended 18:51\n\nIn report you\'ll have "18h - 10min"\n---\n\nTo quit, press Ctrl-Q\n',
    'author': 'Mykola Grechukh-Lezhnov',
    'author_email': 'nick.grechukh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mgrechukh/eltime',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
