# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ms2ml',
 'ms2ml.data',
 'ms2ml.data.adapters',
 'ms2ml.data.parsing',
 'ms2ml.metrics',
 'ms2ml.unimod',
 'ms2ml.utils']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'importlib-metadata>=6.0.0,<7.0.0',
 'lark>=1.1.2,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'lxml>=4.9.1,<5.0.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'psims>=1.2.3,<2.0.0',
 'pyteomics>=4.5.5,<5.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'uniplot>=0.7,<0.9']

extras_require = \
{':python_version >= "3.8" and python_version < "3.11"': ['pandas-stubs>=1.5.1.221024,<2.0.0.0']}

setup_kwargs = {
    'name': 'ms2ml',
    'version': '0.0.34',
    'description': 'Provides an intermediate layer between mass spec data and ML applications, such as encoding.',
    'long_description': 'None',
    'author': 'J. Sebastian Paez',
    'author_email': 'jspaezp@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>3.8,<3.12',
}


setup(**setup_kwargs)
