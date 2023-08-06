# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torippy', 'torippy.gui']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=9.4.0,<10.0.0', 'pyautogui>=0.9.53,<0.10.0']

setup_kwargs = {
    'name': 'torippy',
    'version': '0.1.3',
    'description': '',
    'long_description': '# poetry-template\n\n\n## 概要\n自分用のpoetryプロジェクトのテンプレート。\n\n\n## つかいかた\ncloneしてよしなに。\n\n以下のようなシェルスクリプトを作ってPathを通しておくと、`poetry-template [project-name]` で「templateのclone」・「フォルダのrename」・「vscodeで開く」までできて楽。\n```ps1\n# poetry-template.ps1\nParam ([string]$projectName)\n\ngit clone https://github.com/torippy1024/poetry-template\nRename-Item poetry-template $projectName\ncode $projectName\n```\n\n## 機能\n* vscodeでファイル保存時、自動フォーマット (black)\n* `task run`: src/main.py を実行\n* `task lint`: flake8 で lint\n* `task build`: pyinstaller で exe化\n* `task build-one`: pyinstaller で exe化 (＋ 1つのファイルにまとめる) \n* `task test`: pytest 実行\n\n',
    'author': 'torippy',
    'author_email': '47879788+torippy1024@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
