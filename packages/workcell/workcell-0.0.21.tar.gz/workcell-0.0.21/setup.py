# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['workcell',
 'workcell.api',
 'workcell.cli',
 'workcell.core',
 'workcell.integrations.types',
 'workcell.templates.runtime.custom.app',
 'workcell.templates.runtime.python3.8',
 'workcell.templates.runtime.python3.9',
 'workcell.templates.scaffold.python3.8',
 'workcell.ui']

package_data = \
{'': ['*'], 'workcell': ['templates/runtime/custom/*']}

install_requires = \
['colorama>=0.4.6,<0.5.0',
 'docker>=6.0.1,<7.0.0',
 'fastapi>=0.85.1,<0.86.0',
 'jsonpickle>=3.0.1,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'mangum>=0.17.0,<0.18.0',
 'pandas>=1.5.2,<2.0.0',
 'perspective-python>=1.9.3,<2.0.0',
 'plotly>=5.12.0,<6.0.0',
 'poetry-bumpversion>=0.3.0,<0.4.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'streamlit>=1.15.2,<2.0.0',
 'typer>=0.3.1,<0.4.0',
 'uvicorn>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['workcell = workcell.cli:cli']}

setup_kwargs = {
    'name': 'workcell',
    'version': '0.0.21',
    'description': 'Turn python function into microservice.',
    'long_description': '<!-- markdownlint-disable MD033 MD041 -->\n<h1 align="center">\n    Workcell\n</h1>\n\n<p align="center">\n    <strong>Instantly turn your Python function into production-ready microservice.</strong>\n</p>\n\n<p align="center">\n    <a href="https://pypi.org/project/workcell/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/workcell?color=green&style=flat"></a>\n    <a href="https://github.com/weanalyze/workcell/actions/workflows/release.yml" title="PyPi Version"><img src="https://github.com/weanalyze/workcell/actions/workflows/release.yml/badge.svg"></a> \n    <a href="https://github.com/weanalyze/workcell/actions/workflows/build-image.yml" title="PyPi Version"><img src="https://github.com/weanalyze/workcell/actions/workflows/build-image.yml/badge.svg"></a>     \n    <a href="https://pypi.org/project/workcell/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.8%2B-blue&style=flat"></a>\n    <a href="https://github.com/weanalyze/workcell/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-Apache2.0-blue.svg"></a>\n    <a href="https://weanalyze.co">\n        <img alt="website" src="https://img.shields.io/website/https/weanalyze.co?down_color=red&down_message=offline&up_message=online">\n    </a>    \n    <a href="https://discord.gg/jZuDU5mQZ7">\n        <img alt="discord" src="https://img.shields.io/discord/1004913083812167811?label=discord">\n    </a>      \n</p>\n\n<h4 align="center">\n    <p>\n        <b>English</b> |\n        <a href="https://github.com/weanalyze/workcell/blob/main/README_zh-hans.md">简体中文</a> \n    <p>\n</h4>\n\n<p align="center">\n  <a href="#getting-started">Getting Started</a> •\n  <a href="#license">License</a> •\n  <a href="https://github.com/weanalyze/workcell/releases">Changelog</a>\n</p>\n\nInstantly turn your Python function into production-ready microservice, with lightweight UI to interact with. Use / Share / Publish / Collaborate with your team. \n\n<img align="center" style="width: 100%" src="https://github.com/weanalyze/weanalyze-resources/blob/main/assets/workcell_intro.png?raw=true"/>\n\n---\n\n## Highlights\n\n- \U0001fa84&nbsp; Turn functions into production-ready services within seconds.\n- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.\n- 📦&nbsp; Deploy microservice into weanalye FaaS cloud.\n- 🧩&nbsp; Reuse pre-defined templates & combine with existing components.\n- 📈&nbsp; Instantly deploy and scale for production usage.\n\n## Status\n\n| Status | Stability | Goal |\n| ------ | ------ | ---- |\n| ✅ | Alpha | We are testing Workcell with a closed set of customers |\n| 🚧 | Public Alpha | Anyone can sign up over at weanalyze.co. But go easy on us, there are a few kinks. |\n| ❌ | Public Beta | Stable enough for most non-enterprise use-cases |\n| ❌ | Public | Production-ready |\n\nWe are currently in Alpha. \n\n## Requirements\n\nPython 3.8+\n\n## Installation\n\nRecomended: First activate your virtual environment, with your favourite system. For example, we like poetry and conda!\n\n```bash\npip install workcell\n```\n\n## Getting Started\n\n1. A simple workcell-compatible function could look like this:\n\n    ```python\n    from pydantic import BaseModel\n\n    class Input(BaseModel):\n        message: str\n\n    class Output(BaseModel):\n        message: str\n\n    def hello_workcell(input: Input) -> Output:\n        """Returns the `message` of the input data."""\n        return Output(message=input.message)\n    ```\n\n    _💡 A workcell-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._\n\n2. Copy this code to a file named `app.py`, put into a folder, e.g. `hello_workcell`\n\n3. Run the HTTP API server from command-line:\n\n    ```bash\n    cd hello_workcell\n    workcell serve app:hello_workcell\n    ```\n    _In the output, there\'s a line that shows where your API is being served, on your local machine._\n\n4. Run the Streamlit based UI server from command-line:\n\n    ```bash\n    workcell serve-ui app:hello_workcell\n    ```\n    _In the output, there\'s a line that shows where your UI is being served, on your local machine._\n\n5. **Deploy workcell into weanalyze cloud:**\n\n   🚧 Working in progress, will be updated soon...\n\n## Examples\n\n💡 Find out more usage information and get inspired by our [examples](https://github.com/weanalyze/workcell/tree/main/examples).\n\n## Roadmap\n\n🗓️ Missing a feature? Have a look at our [public roadmap](https://github.com/orgs/weanalyze/projects/5/) to see what the team is working on in the short and medium term. Still missing it? Please let us know by opening an issue!\n\n## Contacts\n\n❓ If you have any questions about the workcell or weanalyze , feel free to email us at: support@weanalyze.co\n\n🙋🏻 If you want to say hi, or are interested in partnering with us, feel free to reach us at: contact@weanalyze.co\n\n😆 Feel free to share memes or any questions at Discord: https://discord.gg/jZuDU5mQZ7\n\n## License\n\nApache-2.0 License.\n',
    'author': 'jiandong',
    'author_email': 'jiandong@weanalyze.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
