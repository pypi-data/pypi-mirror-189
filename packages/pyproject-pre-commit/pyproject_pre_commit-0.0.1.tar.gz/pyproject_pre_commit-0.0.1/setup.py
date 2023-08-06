# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyproject_pre_commit']

package_data = \
{'': ['*']}

install_requires = \
['autoflake==2.0.0',
 'autopep8==2.0.1',
 'bandit[toml]==1.7.4',
 'black==22.12.0',
 'blacken-docs==1.13.0',
 'flake8-annotations-complexity==0.0.7',
 'flake8-bugbear==23.1.20',
 'flake8-builtins==2.1.0',
 'flake8-comprehensions==3.10.1',
 'flake8-debugger==4.1.2',
 'flake8-docstrings==1.7.0',
 'flake8-executable==2.1.3',
 'flake8-pep3101>=2.0.0,<3.0.0',
 'flake8-print==5.0.0',
 'flake8-pyproject==1.2.2',
 'flake8-rst-docstrings==0.3.0',
 'flake8-string-format==0.3.0',
 'isort==5.12.0',
 'mdformat-footnote==0.1.1',
 'mdformat-frontmatter==0.4.1',
 'mdformat-gfm==0.3.5',
 'mdformat==0.7.16',
 'mypy==0.991',
 'pep8-naming==0.13.3',
 'pre-commit-hooks==4.4.0',
 'pre-commit==2.21.0',
 'pycodestyle==2.10.0',
 'shellcheck-py==0.9.0.2']

entry_points = \
{'console_scripts': ['ppc = pyproject_pre_commit:main']}

setup_kwargs = {
    'name': 'pyproject-pre-commit',
    'version': '0.0.1',
    'description': '',
    'long_description': 'None',
    'author': 'rcmdnk',
    'author_email': 'rcmdnk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
