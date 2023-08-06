# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['advance_common']

package_data = \
{'': ['*']}

install_requires = \
['pymavlink>=2.4.37,<3.0.0', 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'advance-common',
    'version': '1.0.0',
    'description': '',
    'long_description': 'Contains files useful on PA and GS:\n- protobuf definition AND compiled python\n- custom mavlink frame code\n- logger setup\n\n# Protobuf messages in messages_pb2 are tracked by git, so when importing this repo as submodule # there is no need to compile protobuf.\n\n# How to use this cool project\n\nPoetry:\n```poetry add git+ssh://git@gitlab.com:academic-aviation-club/sae-2023/advance_common.git```\n\nPip:\n```pip install git+ssh://git@gitlab.com/academic-aviation-club/sae-2023/advance_common.git```\n\nNotice the / instead of : for just pip, for me it only worked this way',
    'author': 'Szymon-SR',
    'author_email': 'srszymonsr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
