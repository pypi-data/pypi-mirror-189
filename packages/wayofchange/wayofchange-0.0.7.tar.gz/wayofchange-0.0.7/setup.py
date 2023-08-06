# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wayofchange']

package_data = \
{'': ['*'], 'wayofchange': ['.idea/*', '.idea/inspectionProfiles/*', 'fonts/*']}

install_requires = \
['os', 'pdf2image', 'pdfCropMargins', 'python-polylabel', 'pyx', 'tqdm']

setup_kwargs = {
    'name': 'wayofchange',
    'version': '0.0.7',
    'description': 'Python suite for music theory analysis and LaTeX outputs.',
    'long_description': 'Read me now',
    'author': 'Edrihan Levesque',
    'author_email': 'edrihan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
