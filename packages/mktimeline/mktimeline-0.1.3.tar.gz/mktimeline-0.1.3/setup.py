# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mktimeline',
 'mktimeline.console',
 'mktimeline.console.commands',
 'mktimeline.events',
 'mktimeline.templates',
 'mktimeline.timeline']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'Markdown>=3.4.1,<4.0.0',
 'beautifulsoup4>=4.11.2,<5.0.0',
 'cleo>=0.8.1,<0.9.0',
 'python-frontmatter>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['mktimeline = mktimeline.console.application:main']}

setup_kwargs = {
    'name': 'mktimeline',
    'version': '0.1.3',
    'description': '',
    'long_description': '# MKTimeline - a static site generator for interactive/visual timelines\nA tool for creating interactive/visual timelines.\n\nThis tool is under development and is considered BETA.\nAs you can see, there is no documentation yet.\nUse at your own risk and befuddlement.\n',
    'author': 'John Duprey',
    'author_email': '297628+jduprey@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jduprey/mktimeline',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1',
}


setup(**setup_kwargs)
