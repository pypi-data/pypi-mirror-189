# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neon_homeassistant_skill']

package_data = \
{'': ['*'], 'neon_homeassistant_skill': ['en-us/*', 'vocab/en-us/*']}

install_requires = \
['pfzy>=0.3.4,<0.4.0']

entry_points = \
{'console_scripts': ['neon-homeassistant-skill = '
                     'neon_homeassistant_skill:NeonHomeAssistantSkill']}

setup_kwargs = {
    'name': 'neon-homeassistant-skill',
    'version': '0.0.6',
    'description': 'A Neon AI Skill for Home Assistant, which integrates with ovos-PHAL-plugin-homeassistant.',
    'long_description': "# Home Assistant Neon Skill\n\nUses [PHAL Home Assistant plugin](https://github.com/OpenVoiceOS/ovos-PHAL-plugin-homeassistant)\n\nStill a work in progress - but for turning devices on/off and opening the Home Assistant dashboard (when using neon-gui), it works!\n\n`pip install neon-homeassistant-skill`\n\n## Upcoming Features\n\n- Color settings (still in testing)\n- Start OAuth workflow with voice\n- Start an instance of the ovos-PHAL-plugin-homeassistant if PHAL isn't already running\n",
    'author': 'Mike Gray',
    'author_email': 'mike@graywind.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
