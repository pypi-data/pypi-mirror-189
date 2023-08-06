# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_xml',
 'pydantic_xml.element',
 'pydantic_xml.element.native',
 'pydantic_xml.serializers',
 'pydantic_xml.serializers.factories']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0']

extras_require = \
{'docs': ['furo>=2022.12.7,<2023.0.0',
          'Sphinx>=5.3.0,<6.0.0',
          'sphinx-copybutton>=0.5.1,<0.6.0',
          'sphinx_design>=0.3.0,<0.4.0',
          'toml>=0.10.2,<0.11.0'],
 'lxml': ['lxml>=4.9.1,<5.0.0']}

setup_kwargs = {
    'name': 'pydantic-xml',
    'version': '0.6.0',
    'description': 'pydantic xml extension',
    'long_description': '\npydantic-xml extension\n======================\n\n.. image:: https://static.pepy.tech/personalized-badge/pydantic-xml?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads/month\n    :target: https://pepy.tech/project/pydantic-xml\n    :alt: Downloads/month\n.. image:: https://github.com/dapper91/pydantic-xml/actions/workflows/test.yml/badge.svg?branch=master\n    :target: https://github.com/dapper91/pydantic-xml/actions/workflows/test.yml\n    :alt: Build status\n.. image:: https://img.shields.io/pypi/l/pydantic-xml.svg\n    :target: https://pypi.org/project/pydantic-xml\n    :alt: License\n.. image:: https://img.shields.io/pypi/pyversions/pydantic-xml.svg\n    :target: https://pypi.org/project/pydantic-xml\n    :alt: Supported Python versions\n.. image:: https://codecov.io/gh/dapper91/pydantic-xml/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/dapper91/pydantic-xml\n    :alt: Code coverage\n.. image:: https://readthedocs.org/projects/pydantic-xml/badge/?version=stable&style=flat\n   :alt: ReadTheDocs status\n   :target: https://pydantic-xml.readthedocs.io/en/stable/\n\n\n``pydantic-xml`` is a `pydantic <https://docs.pydantic.dev>`_ extension providing model fields xml binding\nand xml serialization / deserialization.\nIt is closely integrated with ``pydantic`` which means it supports most of its features.\n\n\nFeatures\n--------\n\n- flexable attributes, elements and text binding\n- python collection types support (``Dict``, ``List``, ``Set``, ``Tuple``, ...)\n- ``Union`` type support\n- pydantic `generic <https://pydantic-docs.helpmanual.io/usage/models/#generic-models>`_ models support\n- `lxml <https://lxml.de/>`_ xml parser support\n- ``xml.etree.ElementTree`` standard library xml parser support\n\nWhat is not supported?\n______________________\n\n- `dynamic model creation <https://docs.pydantic.dev/usage/models/#dynamic-model-creation>`_\n- `dataclasses <https://docs.pydantic.dev/usage/dataclasses/>`_\n- `discriminated unions <https://docs.pydantic.dev/usage/types/#discriminated-unions-aka-tagged-unions>`_\n\nGetting started\n---------------\n\nThe following model fields binding:\n\n.. code-block:: python\n\n   class Product(BaseXmlModel):\n       status: Literal[\'running\', \'development\'] = attr()  # extracted from the \'status\' attribute\n       launched: Optional[int] = attr()  # extracted from the \'launched\' attribute\n       title: str  # extracted from the element text\n\n\n   class Company(BaseXmlModel):\n       trade_name: str = attr(name=\'trade-name\')  # extracted from the \'trade-name\' attribute\n       website: HttpUrl = element()  # extracted from the \'website\' element text\n       products: List[Product] = element(tag=\'product\')  # extracted from the \'website\' element\n\ndefines the XML document:\n\n.. code-block:: xml\n\n   <Company trade-name="SpaceX">\n       <website>https://www.spacex.com</website>\n       <product status="running" launched="2013">Several launch vehicles</product>\n       <product status="running" launched="2019">Starlink</product>\n       <product status="development">Starship</product>\n   </Company>\n\n\nCheck `documentation <https://pydantic-xml.readthedocs.io/en/latest/>`_ for more information.\n',
    'author': 'Dmitry Pershin',
    'author_email': 'dapper1291@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dapper91/pydantic-xml',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
