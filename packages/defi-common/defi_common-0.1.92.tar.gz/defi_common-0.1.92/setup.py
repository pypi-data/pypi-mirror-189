# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['defi_common', 'defi_common.database']

package_data = \
{'': ['*']}

install_requires = \
['alembic>=1.9.2,<2.0.0',
 'asyncpg>=0.27.0,<0.28.0',
 'fastapi-users[sqlalchemy]>=10.3.0,<11.0.0',
 'pre-commit>=2.20.0,<3.0.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'sqlalchemy>=1.4.44,<2.0.0']

setup_kwargs = {
    'name': 'defi-common',
    'version': '0.1.92',
    'description': '',
    'long_description': 'None',
    'author': 'Tomas Toth',
    'author_email': 'tomas.toth004@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
