# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alchemysdk', 'alchemysdk.api', 'alchemysdk.endpoints', 'alchemysdk.types']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=3.0,<4.0', 'aiohttp>=3.8,<4.0']

setup_kwargs = {
    'name': 'alchemysdk',
    'version': '0.1.0',
    'description': 'An unofficial Python SDK for the Alchemy API',
    'long_description': "# Python SDK for the Alchemy API\n\n![python](https://github.com/FastestMolasses/alchemy-sdk/actions/workflows/main.yaml/badge.svg)\n\nAn unofficial Python SDK for the [Alchemy API](https://docs.alchemy.com/).\n\n\n## Installation\n\nRequirements: Python 3.9+\n\nPip:\n```bash\npip install alchemy-sdk\n```\n\nPoetry:\n```bash\npoetry add alchemy-sdk\n```\n\n### Upgrade\n\nPip:\n```bash\npip install alchemy-sdk -U\n```\n\nPoetry:\n```bash\npoetry update alchemy-sdk\n```\n\n## Contributing\n\n1. Fork it (<https://github.com/FastestMolasses/alchemy-sdk/fork>)\n2. Create your feature branch (`git checkout -b feature/fooBar`)\n3. Commit your changes (`git commit -am 'Add some fooBar'`)\n4. Push to the branch (`git push origin feature/fooBar`)\n5. Create a new Pull Request\n",
    'author': 'Abe M',
    'author_email': 'abe.malla8@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FastestMolasses/alchemy-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
