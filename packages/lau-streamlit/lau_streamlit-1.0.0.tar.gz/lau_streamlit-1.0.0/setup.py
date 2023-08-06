# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lau_streamlit']

package_data = \
{'': ['*']}

install_requires = \
['odmantic>=0.9.2,<0.10.0',
 'ply>=3.11,<4.0',
 'pydantic>=1.10.4,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'streamlit-aggrid>=0.3.3,<0.4.0',
 'streamlit>=1.17.0,<2.0.0',
 'watchdog>=2.2.1,<3.0.0']

setup_kwargs = {
    'name': 'lau-streamlit',
    'version': '1.0.0',
    'description': '',
    'long_description': '\n# LAU - Life Avail Utils\n\n## Plang Module - Program Languages\n\n### Dependências \n\n** lau_utils - \n```\npoetry add git+https://github.com/renatocarnauba/lau_utils.git\n```\n',
    'author': 'Renato Carnauba',
    'author_email': 'contato@renatocarnauba.com.br',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
