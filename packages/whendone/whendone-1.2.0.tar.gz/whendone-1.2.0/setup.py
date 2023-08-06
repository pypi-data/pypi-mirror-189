# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['whendone']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0', 'slack-sdk>=3.19.5,<4.0.0']

setup_kwargs = {
    'name': 'whendone',
    'version': '1.2.0',
    'description': 'Python package to notify you when your function is done through Telegram and/or Slack!',
    'long_description': "# WhenDone\n\nPython package to notify you when your function is done through Telegram and/or Slack!\n\n## Installation\n\n```bash\n$ pip install whendone\n```\n\n## Usage\n\n---------\n#### Telegram Example\n---------\n\nFirst create a bot through ``@BotFather``\nStart a conversation with the bot, only once required, ``/start``.\nObtain the token and add it, see code below.\n```python\n  # Import library\n  from whendone import WhenDone\n  # Initialize\n  notifier = WhenDone(telegram_token='XXXXXXXXXXX')\n  \n \n  # Add decorator to function\n  @notifier.whendone\n  def Test():\n      print('Hello World')\n  \n  # Function call\n  Test()\n```\n\n---------\n\n#### Slack Example\n\n---------\nBrowse to ``https://api.slack.com/apps`` create a new app from scratch, give it a name and assign it to a group or person. On the app page, browse to ``OAuth & Permissions``, go to Scope and the following scope, ``chat:write``, reinstall the app and obtain the ``token``. From slack open the chatbot, and obtain the ``id``\n\nThe code is almost the same to the Telegram example, but with the addition of 1 line.\n\n---------\n\n```python\n  # Import library\n  from whendone import WhenDone\n  # Initialize\n  notifier = WhenDone(slack_token='XXXXXXXXXXX')\n  notifier.addSlackChatID('XXXXX')\n \n  # Add decorator to function\n  @notifier.whendone\n  def Test():\n      print('Hello World')\n  \n  # Function call\n  Test()\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms. If you like it, don't forget to give it a ⭐!\n\n## License\n\n`WhenDone` was created by Sabri Barac. It is licensed under the terms of the MIT license.\n\n",
    'author': 'Sabri Barac',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
