# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ray_chunkit_chung_gum_gum_pistol']

package_data = \
{'': ['*']}

install_requires = \
['pytest[all]>=7.2.1,<8.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['gum = ray_chunkit_chung_gum_gum_pistol.main:app']}

setup_kwargs = {
    'name': 'ray-chunkit-chung-gum-gum-pistol',
    'version': '0.1.1',
    'description': '',
    'long_description': '# gum gum pistol\n\nMinimal example to create a pypi package using poetry\n\n<https://pypi.org/project/ray-chunkit-chung-gum-gum-pistol/>\n\n![image](https://user-images.githubusercontent.com/26511618/216767867-50a63a7f-bb39-4020-9227-e6672c454c9a.png)\n(Screen cap from <https://onepiece.fandom.com/wiki/Gomu_Gomu_no_Mi/Techniques>)\n\n## How to use\n\nInstall gum-gum-pistol\n\n```bash\npip install ray-chunkit-chung-gum-gum-pistol\n```\n\nThis gum-gum-pistol has two functions\n\n```bash\ngum load\ngum shoot\n```\n\nThat\'s it!\n\n## Use typer to create gum-gum-pistol\n\n<https://typer.tiangolo.com/tutorial/package/>\n\n### Step 1 Install python\n\n```bash\npython -m venv .venv\n# .venv\\Scripts\\activate\nsource .venv/bin/activate\npython -m pip install --upgrade pip\npip install --upgrade -r requirements.txt\n```\n\n### Step 2 Init project and dependencies\n\n```bash\npoetry new ray-chunkit-chung-gum-gum-pistol\ncd ray-chunkit-chung-gum-gum-pistol\npoetry add typer[all]\npoetry add pytest[all]\n```\n\n### Step 3 Define app\n\nDefine app path\n\n```toml\n[tool.poetry.scripts]\ngum = "ray_chunkit_chung_gum_gum_pistol.main:app"\n```\n\nInstall local for test\n\n```bash\npoetry install\n```\n\nTest app local\n\n```bash\ngum --help\ngum load\ngum shoot\n```\n\n### Step 4 Distribute app\n\nBuild wheel file\n\n```bash\npoetry build\n```\n\nTest by changing to a new venv and install from local dist\n\n```bash\npip install ray-chunkit-chung-gum-gum-pistol\\dist\\ray_chunkit_chung_gum_gum_pistol-0.1.0-py3-none-any.whl\n```\n\n### Step 5 Upload to pypi\n\nCreate PYPI_TOKEN and export to env. Then config pypi-token in poetry. Then publish to pypi\n\n```bash\npoetry config pypi-token.pypi $PYPI_TOKEN\npoetry publish --build\n```\n\nTest by changing to a new venv and install from pypi\n\n```bash\npip install ray-chunkit-chung-gum-gum-pistol\ngum --help\n```\n',
    'author': 'ray-chunkit-chung',
    'author_email': 'ray.chunkit.chung@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
