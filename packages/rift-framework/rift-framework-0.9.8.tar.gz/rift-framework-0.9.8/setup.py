# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rift',
 'rift.ast',
 'rift.ast.patchers',
 'rift.ast.types',
 'rift.bases',
 'rift.cli',
 'rift.cli.commands',
 'rift.cli.util',
 'rift.core',
 'rift.cst',
 'rift.fift',
 'rift.fift.types',
 'rift.func',
 'rift.func.types',
 'rift.keys',
 'rift.keys.mnemonic',
 'rift.keys.mnemonic.bip39',
 'rift.library',
 'rift.logging',
 'rift.meta',
 'rift.native',
 'rift.network',
 'rift.runtime',
 'rift.types',
 'rift.types.bases',
 'rift.util',
 'rift.wallet']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<6.1',
 'appdirs>=1.4.4,<1.5.0',
 'astpretty>=3.0.0,<3.1.0',
 'click>=8.1.3,<8.2.0',
 'colorful>=0.5.4,<0.6.0',
 'cryptography>=39.0.0,<40.0.0',
 'libcst>=0.4.7,<0.5.0',
 'pynacl>=1.5.0,<2.0.0',
 'rift-tonlib>=0.0.2,<0.0.3',
 'setuptools>=65.6.3,<66.0.0',
 'tomlkit>=0.11.4,<0.12.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['rift = rift.cli.entry:entry']}

setup_kwargs = {
    'name': 'rift-framework',
    'version': '0.9.8',
    'description': 'The magical Python -> TON Portal',
    'long_description': '<img align="left" width="64" height="64" src="https://github.com/sky-ring/rift/blob/main/assets/rift-icon.png">\n\n# Rift\n\n[![PyPI version](https://img.shields.io/badge/rift--framework-0.9.8-informational?style=flat-square&color=FFFF91&labelColor=360825)](https://pypi.org/project/rift-framework/)\n[![Telegram](https://img.shields.io/badge/Telegram-@skyring__org-informational?style=flat-square&color=0088cc&labelColor=360825)](https://t.me/skyring_org)\n[![Telegram](https://img.shields.io/badge/Docs-docs.skyring.io/rift-informational?style=flat-square&color=6A0F49&labelColor=360825)](https://docs.skyring.io/rift/)\n> _A magical **Python3** -> **TON** portal_\n\nRift is smart contract development framework in Python for [TON (The Open Network)](https://ton.org). Its purpose is to make the development, testing, and deployment procedures much easier!\n\n## Goals\n- To be a simple full-stack Python framework for developing on the TON ecosystem\n- Make standard contract implementations available (similar to OpenZeppelin)\n- Utilize Python\'s syntax to provide code reuse, understandable, and organized code that is simple to test\n\n## Overview\nRift\'s main purpose is to make contract building simpler for TON by bypassing the steep learning curve of `FunC`. Rift, by exploiting Python\'s OOP features, will enable you to create with more ease and less worry. In Rift, here is how the [Simple wallet contract](https://github.com/ton-blockchain/ton/blob/master/crypto/smartcont/wallet-code.fc) looks:\n\n```python\nfrom rift import *\n\n\nclass SimpleWallet(Contract):\n    """\n    Simple Wallet Contract.\n\n    # config\n    get-methods:\n        - seq_no\n        - public_key\n    """\n\n    class Data(Model):\n        seq_no: uint32\n        public_key: uint256\n\n    class ExternalBody(Payload):\n        signature: slice[512]\n        seq_no: uint32\n        valid_until: uint32\n\n    data: Data\n\n    def external_receive(\n        self,\n        in_msg: Slice,\n    ) -> None:\n        msg = self.ExternalBody(in_msg)\n        assert msg.valid_until > std.now(), 35\n        assert msg.seq_no == self.data.seq_no, 33\n        assert std.check_signature(\n            msg.hash(after="signature"),\n            msg.signature,\n            self.data.public_key,\n        ), 34\n        std.accept_message()\n        while msg.refs():\n            mode = msg >> uint8\n            std.send_raw_message(msg >> Ref[Cell], mode)\n        self.data.seq_no += 1\n        self.data.save()\n```\n\n## Quick Start\n\n0. Install `Python 3.10+`\n1. Install `rift`\n```bash\npip install rift-framework\n# or from source\ngit clone https://github.com/sky-ring/rift\ncd rift\npip install -e .\n```\n2. Initialize your project:\n```bash\nrift init <project-name>\n```\n3. Start developing your contracts in `<project>/contracts/`\n4. Build contracts and get the `FunC` contracts in `<project>/build/`\n```bash\n# in project folder\nrift build\n```\n\n## Standard Contracts Implementation\n- [x] Jetton Implementation ([jetton-impl](https://github.com/sky-ring/jetton-impl))\n- [ ] NFT Implementation\n- [ ] DEX Implementation\n\n\n## Documentation and Examples\nFull documentation with specifications is being developed and will be available shortly!\nUntil then, you may look at standard contracts implementation; they cover the majority of the ideas required; if you\'re looking for more, take a glance at the \'test/\' directory for some demonstrations of Rift\'s capabilities.\n\n## Roadmap\n\n### Milestone 1: Python Framework for contract development\n\n- [x] Semi One-to-One mapping of functions and expressions (Base Compiler, Python -> FunC)\n- [x] First higher layer over the base mappings to simplify type calls (leveraging OOP capabilities)\n- [x] Second higher layer over the base, simplifying contract developments towards maximizing code reusability and simplicity (leveraging Meta programming capabilities)\n- [x] Providing standard smart contracts implementation with Rift\n\n### Milestone 2: deploying, testing, interaction capabilities\n- [x] Simple interaction interface with TON Blockchain\n- [x] Simple deploying options of developed contracts\n- [x] Testing framework for the contracts developed with Rift\n\n## Contributing\nIf you\'re interested in contributing to Rift, please see [CONTRIBUTING.md](https://github.com/sky-ring/rift/blob/main/CONTRIBUTING.md) for the necessary specifications and procedure.\n\n## Supporters\nSpecial thanks to the [TON Society](https://society.ton.org/) for their support and grant, without which the project would not be feasible.\n',
    'author': 'Amin Rezaei',
    'author_email': 'AminRezaei0x443@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
