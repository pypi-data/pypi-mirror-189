# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['box']

package_data = \
{'': ['*']}

extras_require = \
{'all': ['msgpack>=1.0.0', 'ruamel.yaml>=0.17', 'tomli-w>=1.0.0'],
 'all:python_version < "3.11"': ['tomli>=1.2.3'],
 'msgpack': ['msgpack>=1.0.0'],
 'pyyaml': ['PyYAML>=6.0'],
 'ruamel-yaml': ['ruamel.yaml>=0.17'],
 'toml': ['toml>=0.10.2'],
 'tomli': ['tomli-w>=1.0.0'],
 'tomli:python_version < "3.11"': ['tomli>=1.2.3'],
 'yaml': ['ruamel.yaml>=0.17']}

setup_kwargs = {
    'name': 'python-box',
    'version': '7.0.0',
    'description': 'Advanced Python dictionaries with dot notation access',
    'long_description': '|BuildStatus| |License|\n\n|BoxImage|\n\n.. code:: python\n\n        from box import Box\n\n        movie_box = Box({ "Robin Hood: Men in Tights": { "imdb stars": 6.7, "length": 104 } })\n\n        movie_box.Robin_Hood_Men_in_Tights.imdb_stars\n        # 6.7\n\n\nBox will automatically make otherwise inaccessible keys safe to access as an attribute.\nYou can always pass `conversion_box=False` to `Box` to disable that behavior.\nAlso, all new dict and lists added to a Box or BoxList object are converted automatically.\n\nThere are over a half dozen ways to customize your Box and make it work for you.\n\nCheck out the new `Box github wiki <https://github.com/cdgriffith/Box/wiki>`_ for more details and examples!\n\nInstall\n=======\n\n**Version Pin Your Box!**\n\nIf you aren\'t in the habit of version pinning your libraries, it will eventually bite you.\nBox has a `list of breaking change <https://github.com/cdgriffith/Box/wiki/Major-Version-Breaking-Changes>`_ between major versions you should always check out before updating.\n\nrequirements.txt\n----------------\n\n.. code:: text\n\n        python-box[all]~=7.0\n\nAs Box adheres to semantic versioning (aka API changes will only occur on between major version),\nit is best to use `Compatible release <https://www.python.org/dev/peps/pep-0440/#compatible-release>`_ matching using the `~=` clause.\n\nInstall from command line\n-------------------------\n\n.. code:: bash\n\n        python -m pip install --upgrade pip\n        pip install python-box[all]~=7.0 --upgrade\n\nInstall with selected dependencies\n----------------------------------\n\nBox does not install external dependencies such as yaml and toml writers. Instead you can specify which you want,\nfor example, `[all]` is shorthand for:\n\n.. code:: bash\n\n        pip install python-box[ruamel.yaml,tomli_w,msgpack]~=7.0 --upgrade\n\nBut you can also sub out `ruamel.yaml` for `PyYAML`.\n\nCheck out `more details <https://github.com/cdgriffith/Box/wiki/Installation>`_ on installation details.\n\nBox 7 is tested on python 3.7+, if you are upgrading from previous versions, please look through\n`any breaking changes and new features <https://github.com/cdgriffith/Box/wiki/Major-Version-Breaking-Changes>`_.\n\nOptimized Version\n-----------------\n\nBox has introduced Cython optimizations for major platforms by default.\nLoading large data sets can be up to 10x faster!\n\nIf you are **not** on a x86_64 supported system you will need to do some extra work to install the optimized version.\nThere will be an warning of "WARNING: Cython not installed, could not optimize box" during install.\nYou will need python development files, system compiler, and the python packages `Cython` and `wheel`.\n\n**Linux Example:**\n\nFirst make sure you have python development files installed (`python3-dev` or `python3-devel` in most repos).\nYou will then need `Cython` and `wheel` installed and then install (or re-install with `--force`) `python-box`.\n\n.. code:: bash\n\n        pip install Cython wheel\n        pip install python-box[all]~=7.0 --upgrade --force\n\nIf you have any issues please open a github issue with the error you are experiencing!\n\nOverview\n========\n\n`Box` is designed to be a near transparent drop in replacements for\ndictionaries that add dot notation access and other powerful feature.\n\nThere are a lot of `types of boxes <https://github.com/cdgriffith/Box/wiki/Types-of-Boxes>`_\nto customize it for your needs, as well as handy `converters <https://github.com/cdgriffith/Box/wiki/Converters>`_!\n\nKeep in mind any sub dictionaries or ones set after initiation will be automatically converted to\na `Box` object, and lists will be converted to `BoxList`, all other objects stay intact.\n\nCheck out the `Quick Start <https://github.com/cdgriffith/Box/wiki/Quick-Start>`_  for more in depth details.\n\n`Box` can be instantiated the same ways as `dict`.\n\n.. code:: python\n\n        Box({\'data\': 2, \'count\': 5})\n        Box(data=2, count=5)\n        Box({\'data\': 2, \'count\': 1}, count=5)\n        Box([(\'data\', 2), (\'count\', 5)])\n\n        # All will create\n        # <Box: {\'data\': 2, \'count\': 5}>\n\n`Box` is a subclass of `dict` which overrides some base functionality to make\nsure everything stored in the dict can be accessed as an attribute or key value.\n\n.. code:: python\n\n      small_box = Box({\'data\': 2, \'count\': 5})\n      small_box.data == small_box[\'data\'] == getattr(small_box, \'data\')\n\nAll dicts (and lists) added to a `Box` will be converted on insertion to a `Box` (or `BoxList`),\nallowing for recursive dot notation access.\n\n`Box` also includes helper functions to transform it back into a `dict`,\nas well as into `JSON`, `YAML`, `TOML`, or `msgpack` strings or files.\n\n\nThanks\n======\n\nA huge thank you to everyone that has given features and feedback over the years to Box! Check out everyone that has contributed_.\n\nA big thanks to Python Software Foundation, and PSF-Trademarks Committee, for official approval to use the Python logo on the `Box` logo!\n\nAlso special shout-out to PythonBytes_, who featured Box on their podcast.\n\n\nLicense\n=======\n\nMIT License, Copyright (c) 2017-2023 Chris Griffith. See LICENSE_ file.\n\n\n.. |BoxImage| image:: https://raw.githubusercontent.com/cdgriffith/Box/master/box_logo.png\n   :target: https://github.com/cdgriffith/Box\n.. |BuildStatus| image:: https://github.com/cdgriffith/Box/workflows/Tests/badge.svg?branch=master\n   :target: https://github.com/cdgriffith/Box/actions?query=workflow%3ATests\n.. |License| image:: https://img.shields.io/pypi/l/python-box.svg\n   :target: https://pypi.python.org/pypi/python-box/\n\n.. _PythonBytes: https://pythonbytes.fm/episodes/show/19/put-your-python-dictionaries-in-a-box-and-apparently-python-is-really-wanted\n.. _contributed: AUTHORS.rst\n.. _`Wrapt Documentation`: https://wrapt.readthedocs.io/en/latest\n.. _reusables: https://github.com/cdgriffith/reusables#reusables\n.. _created: https://github.com/cdgriffith/Reusables/commit/df20de4db74371c2fedf1578096f3e29c93ccdf3#diff-e9a0f470ef3e8afb4384dc2824943048R51\n.. _LICENSE: https://github.com/cdgriffith/Box/blob/master/LICENSE\n',
    'author': 'Chris Griffith',
    'author_email': 'chris@cdgriffith.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cdgriffith/Box',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
