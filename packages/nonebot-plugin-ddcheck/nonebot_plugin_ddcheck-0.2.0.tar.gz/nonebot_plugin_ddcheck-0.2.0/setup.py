# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_ddcheck']

package_data = \
{'': ['*'], 'nonebot_plugin_ddcheck': ['template/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'httpx>=0.19.0',
 'nonebot-adapter-onebot>=2.2.0,<3.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot-plugin-htmlrender>=0.0.4',
 'nonebot-plugin-localstore>=0.3.0,<0.4.0',
 'nonebot2[fastapi]>=2.0.0-rc.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ddcheck',
    'version': '0.2.0',
    'description': 'Nonebot2 成分姬插件',
    'long_description': '# nonebot-plugin-ddcheck\n\nNoneBot2 成分姬插件\n\n查询B站关注列表的VTuber成分，并以图片形式发出\n\nVTB列表数据来源：[vtbs.moe](https://vtbs.moe/)\n\n\n### 使用方式\n\n**以下命令需要加[命令前缀](https://v2.nonebot.dev/docs/api/config#Config-command_start) (默认为`/`)，可自行设置为空**\n\n```\n查成分 + B站用户名/UID\n```\n\n\n### 安装\n\n- 使用 nb-cli\n\n```\nnb plugin install nonebot_plugin_ddcheck\n```\n\n- 使用 pip\n\n```\npip install nonebot_plugin_ddcheck\n```\n\n\n### 配置\n\n需要在 `.env.xxx` 文件中添加任意的B站用户cookie：\n\n```\nbilibili_cookie=xxx\n```\n\n`cookie` 获取方式：\n\n`F12` 打开开发工具，查看 `www.bilibili.com` 请求的响应头，找形如 `SESSDATA=xxx;` 的字段，如：\n\n```\nbilibili_cookie="SESSDATA=xxx;"\n```\n\n<div align="left">\n  <img src="https://s2.loli.net/2022/07/19/AIBmd2Z9V5YwlkF.png" width="500" />\n</div>\n\n\n### 示例\n\n<div align="left">\n  <img src="https://s2.loli.net/2022/03/20/Nk3jZJgxforHDsu.png" width="400" />\n</div>\n',
    'author': 'meetwq',
    'author_email': 'meetwq@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/noneplugin/nonebot-plugin-ddcheck',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
