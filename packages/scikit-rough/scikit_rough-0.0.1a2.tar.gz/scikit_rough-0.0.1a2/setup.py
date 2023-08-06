# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['skrough',
 'skrough.algorithms',
 'skrough.algorithms.hooks',
 'skrough.algorithms.hooks.common',
 'skrough.algorithms.meta',
 'skrough.chaos_measures',
 'skrough.estimators',
 'skrough.structs']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.0.1,<23.0.0',
 'docstring-parser>=0.15,<0.16',
 'joblib>=1.1.0,<2.0.0',
 'more-itertools>=8.14.0,<9.0.0',
 'numba>=0.56.0,<0.57.0',
 'numpy>=1.22.4,<2.0.0',
 'pandas>=1.4.2,<2.0.0',
 'scikit-learn>=1.1.1,<2.0.0']

setup_kwargs = {
    'name': 'scikit-rough',
    'version': '0.0.1a2',
    'description': '',
    'long_description': '[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Documentation Status](https://readthedocs.org/projects/scikit-rough/badge/?version=latest)](https://scikit-rough.readthedocs.io/en/latest/)\n\n\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sebov_scikit-rough&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=sebov_scikit-rough)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=sebov_scikit-rough&metric=coverage)](https://sonarcloud.io/summary/new_code?id=sebov_scikit-rough)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sebov_scikit-rough&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sebov_scikit-rough)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sebov_scikit-rough&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sebov_scikit-rough)\n[![Total alerts](https://img.shields.io/lgtm/alerts/g/sebov/scikit-rough.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sebov/scikit-rough/alerts/)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/sebov/scikit-rough.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sebov/scikit-rough/context:python)\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a1e1457efb4b4b5da569b9c9881f1ca9)](https://www.codacy.com/gh/sebov/scikit-rough/dashboard?utm_source=github.com&utm_medium=referral&utm_content=sebov/scikit-rough&utm_campaign=Badge_Grade)\n[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/a1e1457efb4b4b5da569b9c9881f1ca9)](https://www.codacy.com/gh/sebov/scikit-rough/dashboard?utm_source=github.com&utm_medium=referral&utm_content=sebov/scikit-rough&utm_campaign=Badge_Coverage)\n\n# scikit-rough\n\n**scikit-rough** is a Python package/toolbox of algorithms and functions for data analysis\nbased on the rough set theory\n\nRead [scikit-rough documentation](https://scikit-rough.readthedocs.io/).\n',
    'author': 'sebov',
    'author_email': '12091011+sebov@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
