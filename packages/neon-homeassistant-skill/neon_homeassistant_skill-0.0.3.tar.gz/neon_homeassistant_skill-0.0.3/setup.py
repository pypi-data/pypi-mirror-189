# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neon_homeassistant_skill']

package_data = \
{'': ['*'], 'neon_homeassistant_skill': ['vocab/en-us/*']}

install_requires = \
['pfzy>=0.3.4,<0.4.0']

setup_kwargs = {
    'name': 'neon-homeassistant-skill',
    'version': '0.0.3',
    'description': 'A Neon AI Skill for Home Assistant, which integrates with ovos-PHAL-plugin-homeassistant.',
    'long_description': "# Home Assistant Neon Skill\n\nUses [PHAL Home Assistant plugin](https://github.com/OpenVoiceOS/ovos-PHAL-plugin-homeassistant)\n\nStill a work in progress - please don't expect it to work yet :)\n\n`pip install neon-homeassistant-skill`\n",
    'author': 'Mike Gray',
    'author_email': 'mike@graywind.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
