# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigma', 'sigma.pipelines.sysmon']

package_data = \
{'': ['*']}

install_requires = \
['pysigma>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'pysigma-pipeline-sysmon',
    'version': '1.0.2',
    'description': 'pySigma Sysmon processing pipelines',
    'long_description': 'None',
    'author': 'Thomas Patzke',
    'author_email': 'thomas@patzke.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SigmaHQ/pySigma-pipeline-sysmon/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
