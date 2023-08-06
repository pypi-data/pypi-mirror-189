# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chartstag', 'chartstag.mermaid']

package_data = \
{'': ['*'], 'chartstag.mermaid': ['data/*']}

install_requires = \
['scistag>=0.8.1,<0.9.0']

setup_kwargs = {
    'name': 'chartstag',
    'version': '0.8.1',
    'description': 'Charting and diagram extension for SciStag',
    'long_description': '# ChartStag\n\nChartStag is an extension for the [SciStag](https://github.com/scistag/scistag) package\nwhich supports you in your computer vision, data science and data engineering \nprojects.\n\nIt extends SciStag with diagram and chart plotting capabilities. As of now solely by\nintegrating [mermaid](https://github.com/mermaid-js/mermaid), an awesome diagram and \ncharting tool written in JavaScript, into SciStag VisualLog.\n\nmermaid is licensed under the terms of the [MIT license](https://github.com/mermaid-js/mermaid/blob/develop/LICENSE) -\nfor further details about mermaid visit https://github.com/mermaid-js/mermaid or \nhttps://mermaid.js.org/.\n\nAt this point huge thanks to [Knut Sveidqvist](https://github.com/knsv) and the whole\nmermaid team for their awesome work.\n\n---\n\nChartStag itself is as well licensed under the terms of the MIT license and \nCopyright (c) 2023 [Michael Ikemann](https://github.com/alyxion).\n\nFor examples about how to use ChartStag in SciStag install scistag via `pip install scistag[common]`\nand see https://github.com/SciStag/SciStag/tree/main/scistag/examples/vislog.',
    'author': 'Michael Ikemann',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/scistag/chartstag',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
