# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nessvector']

package_data = \
{'': ['*']}

install_requires = \
['nessvec>=0.0.18,<0.0.19']

entry_points = \
{'console_scripts': ['nessvec = nessvec.main:main']}

setup_kwargs = {
    'name': 'nessvector',
    'version': '1.0.0',
    'description': 'Alias that redirects to nessvec',
    'long_description': "# ALIAS for [nessvec](gitlab.com/tangibleai/nessvec)\n\n## Install from Source (recommended)\n\nClone the repository with all the source code and data:\n\n```console\n$ git clone git@gitlab.com:tangibleai/nessvec\n$ cd nessvec\n```\n\nCreate a conda environment and install the dependencies:\n\n```console\n$ conda create -n nessvec 'python==3.9.7'\n$ conda env update -n nessvec -f scripts/environment.yml\n$ pip install -e .\n```\n\n## Install from PyPi (only tested on Linux)\n\n```console\n$ pip install nessvec\n```\n\n## Get Started\n\n```python\n>>> from nessvec.util import load_glove\n>>> w2v = load_glove()\n>>> seattle = w2v['seattle']\n>>> seattle\narray([-2.7303e-01,  8.5872e-01,  1.3546e-01,  8.3849e-01, ...\n>>> portland = w2v['portland']\n>>> portland\narray([-0.78611  ,  1.2758   , -0.0036066,  0.54873  , -0.31474  ,...\n>>> len(portland)\n50\n>>> from numpy.linalg import norm\n>>> norm(portland)\n4.417...\n>>> portland.std()\n0.615...\n\n```\n\n```\n>>> cosine_similarity(seattle, portland)\n0.84...\n>>> cosine_similarity(portland, seattle)\n0.84...\n\n```\n\n```python\n>>> from nessvec.util import cosine_similarity\n>>> cosine_similarity(w2v['los_angeles'], w2v['mumbai'])\n.5\n\n```\n\n##\n\n",
    'author': 'Hobson Lane',
    'author_email': 'hobson@tangibleai.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/tangibleai/nessvec',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
