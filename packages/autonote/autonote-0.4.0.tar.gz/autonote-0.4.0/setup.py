# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['autonote']

package_data = \
{'': ['*'], 'autonote': ['templates/*']}

install_requires = \
['atlassian-python-api>=3.32.1,<4.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'notion-client>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'autonote',
    'version': '0.4.0',
    'description': 'Automate taking notes',
    'long_description': '# autonote\n\n[![codecov](https://codecov.io/gh/nakamasato/autonote/branch/main/graph/badge.svg?token=ejR44mVdjO)](https://codecov.io/gh/nakamasato/autonote)\n\n## Description\n\n![](docs/diagram.drawio.svg)\n\nAutomate creating daily, weekly, monthly, and quarterly manual repetitive documents:\n\n1. Daily: daily journal, habit tracker\n1. Weekly: weekly report\n1. Monthly: monthly report\n1. Quarterly: quarterly review\n\n## Prerequisite\n\n1. Confluence API Token\n1. Notion Integration Token\n\n## Installation\n\n```\npip install autonote\n```\n\n## Usage (Notion)\n\n```python\nfrom autonote.notion import NotionClient\n\nclient = NotionClient()\n\nkwargs = {\n    "Date": {"start": "2023-02-04", "end": "2023-02-10"},\n    "replace_rules": [\n        {\n            "block_types": ["heading_1"],  # target blocks to apply replacement\n            "replace_str": "YYYY/MM/DD",  # replacement string match\n            "replace_type": "datetime",  # currently only support "datetime"\n            "date_format": "%Y/%m/%d",  # used to parse `start_date` and generate string from datetime when interpolating\n            "start_date": "2023/02/04",  # start date\n            "increment": True,  # if true, increment 1 day every time replacement is executed\n        },\n    ],\n}\nclient.create_page_from_template(\n    template_id="a7cc4f73460c4b9fa82be8d4ed74d8ca",\n    title="weekly note",\n    override=True,\n    **kwargs\n)\n```\n\nTemplate:\n\n<table><tr><td>\n<img src="docs/notion_template_page_1.png" width="200px" />\n</td></tr></table>\n\nGenerated page:\n\n<table><tr><td>\n<img src="docs/notion_page_3.png" width="200px" />\n</td></tr></table>\n\n\nFor more examples, please check [Examples](examples/README.md).\n\n## Credits\n\n`autonote` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`autonote` was created by Masato Naka. It is licensed under the terms of the MIT license.\n\n## References\n1. [Atlassian Python API Confluence module](https://atlassian-python-api.readthedocs.io/confluence.html)\n1. [notion-client](https://pypi.org/project/notion-client/)\n1. [Notion API](https://developers.notion.com/)\n',
    'author': 'Masato Naka',
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
