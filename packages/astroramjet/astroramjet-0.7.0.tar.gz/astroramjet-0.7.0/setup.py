# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ramjet',
 'ramjet.analysis',
 'ramjet.analysis.light_curve_folding_vizualizer',
 'ramjet.analysis.results_viewer',
 'ramjet.analysis.tess_ffi_variability_viewer',
 'ramjet.analysis.viewer',
 'ramjet.data_interface',
 'ramjet.database',
 'ramjet.logging',
 'ramjet.models',
 'ramjet.models.components',
 'ramjet.photometric_database',
 'ramjet.photometric_database.derived',
 'ramjet.photometric_database.setup']

package_data = \
{'': ['*'], 'ramjet.analysis.results_viewer': ['templates/*']}

install_requires = \
['astropy>=5.2.1,<6.0.0',
 'astroquery>=0.4.6,<0.5.0',
 'backports-strenum>=1.1.1,<2.0.0',
 'beautifulsoup4>=4.11.2,<5.0.0',
 'bokeh>=2.4.0,<2.5.0',
 'dataset>=1.6.0,<2.0.0',
 'gitpython>=3.1.30,<4.0.0',
 'lightkurve>=2.3.0,<3.0.0',
 'lxml>=4.9.2,<5.0.0',
 'matplotlib>=3.6.3,<4.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'pathos>=0.3.0,<0.4.0',
 'peewee>=3.15.4,<4.0.0',
 'pipreqs>=0.4.11,<0.5.0',
 'plotly>=5.13.0,<6.0.0',
 'pyarrow>=11.0.0,<12.0.0',
 'pytest-asyncio>=0.20.3,<0.21.0',
 'pytest>=7.2.1,<8.0.0',
 'requests>=2.28.2,<3.0.0',
 'retrying>=1.3.4,<2.0.0',
 'scipy>=1.10.0,<2.0.0',
 'setuptools>=67.1.0,<68.0.0',
 'sphinx-autoapi>=2.0.1,<3.0.0',
 'sphinx-press-theme>=0.8.0,<0.9.0',
 'sphinx>=6.1.3,<7.0.0',
 'tenacity>=8.1.0,<9.0.0',
 'tornado>=6.2,<7.0',
 'uvloop>=0.17.0,<0.18.0',
 'wandb>=0.13.9,<0.14.0']

extras_require = \
{':sys_platform != "darwin" or platform_machine != "arm64"': ['tensorflow>=2.11.0,<3.0.0'],
 ':sys_platform == "darwin" and platform_machine == "arm64"': ['tensorflow-macos>=2.11.0,<3.0.0']}

setup_kwargs = {
    'name': 'astroramjet',
    'version': '0.7.0',
    'description': '',
    'long_description': '![ramjet_engine](docs/ramjet_engine.png)\n\n# RAMjET: RApid MachinE-learned Triage\n\nRAMjET is a framework for producing neural networks to characterize phenomena in astrophysical photometric data.\n\nRAMjET is currently in alpha. This repository is currently oriented toward the RAMjET development team and is not yet intended for a general audience.\n\n[See here for documentation.](https://astroramjet.readthedocs.io/en/latest/)\n',
    'author': 'Greg Olmschenk',
    'author_email': 'greg@olmschenk.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
