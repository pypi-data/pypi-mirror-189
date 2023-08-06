# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xboto']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.64,<2.0.0',
 'botocore>=1.29.64,<2.0.0',
 'xinject>=1.2.0,<2.0.0',
 'xsentinels>=1.2.1,<2.0.0']

setup_kwargs = {
    'name': 'xboto',
    'version': '1.0.0',
    'description': 'Easy lazy dependency injection for boto3 clients/resources.',
    'long_description': "## Xyngular AWS Library\n\nLatest documentation can be reached at [<http://devdocs.xyngular.net/py-xyn-aws/latest/index.html>](<http://devdocs.xyngular.net/py-xyn-aws/latest/index.html>)\n\nAWS utilities to help working aws services and with boto3.\n\n## Quick Start\n\n### Import Boto Client/Resource\n\n```python\n\n# Use imported `dynamodb` just like dynamodb boto resource\nfrom xboto.resource import dynamodb\n\n# Use imported `ssm` just like ssm boto client\nfrom xboto.client import ssm\n\n# These are for overriding/injecting settings.\nfrom xboto import BotoResources, BotoClients, BotoSession\n\n# Can use them like normal:\ndynamodb.table(...)\nssm.get_object(...)\n\n\n# Or you can override settings if you wish:\nwith BotoResources.DynamoDB(region_name='us-west-2'):\n    # Use us-west-2 when using dynamodb boto resource:\n    dynamodb.table(...)\n\nwith BotoClients.Ssm(region_name='us-west-2'):\n    # Use us-west-2 when using ssm boto client:\n    ssm.get_object(...)\n\nwith BotoSession(region_name='us-west-3'):\n    # Use us-west-3 when using any client/resource\n    # we are setting it at the boto-session level;\n    # the session is used by all boto client/resources.\n    ssm.get_object(...)\n\n    \n# Can use them like decorators as well:\n@BotoClients.Ssm(region_name='us-west-2')\ndef some_method():\n    ssm.get_object(...)\n\n```\n\n### Grab Any Client/Resource\n\n```python\n\n# Can easily ask these for any client/resource\nfrom xboto import boto_clients, boto_resources\n\n# These are for overriding/injecting settings.\nfrom xboto import BotoResources, BotoClients, BotoSession\n\n# Can use them like normal:\nboto_clients.dynamodb.table(...)\nboto_resources.ssm.get_object(...)\n\n\n# Or you can override settings if you wish:\nwith BotoResources.DynamoDB(region_name='us-west-2'):\n    # Use us-west-2 when using dynamodb boto resource:\n    boto_resources.dynamodb.table(...)\n\nwith BotoClients.Ssm(region_name='us-west-2'):\n    # Use us-west-2 when using ssm boto client:\n    boto_clients.ssm.get_object(...)\n\nwith BotoSession(region_name='us-west-3'):\n    # Use us-west-3 when using any client/resource\n    # we are setting it at the boto-session level;\n    # the session is used by all boto client/resources.\n    boto_clients.ssm.get_object(...)\n\n    \n# Can use them like decorators as well:\n@BotoClients.Ssm(region_name='us-west-2')\ndef some_method():\n    boto_clients.ssm.get_object(...)\n\n```\n",
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyngular/py-xbool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
