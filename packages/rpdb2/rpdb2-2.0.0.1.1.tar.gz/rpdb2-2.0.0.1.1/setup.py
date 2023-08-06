# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpdb']

package_data = \
{'': ['*']}

modules = \
['rpdb2']
setup_kwargs = {
    'name': 'rpdb2',
    'version': '2.0.0.1.1',
    'description': 'rpdb2 module extracted from winpdb pacage.',
    'long_description': '# rpdb2\n\nrpdb2 module extracted from winpdb package.\n\nIn contrast to winpdb, this module can be installed without wxpython.\n\nNote that it contain rpdb module with may conflict with the one that comes with rpdb package.\n\nVersion of this package is the same as version of winpdb that rpdb2 was stolen from.\n\n',
    'author': 'Philippe Fremy, Nir Aides',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
