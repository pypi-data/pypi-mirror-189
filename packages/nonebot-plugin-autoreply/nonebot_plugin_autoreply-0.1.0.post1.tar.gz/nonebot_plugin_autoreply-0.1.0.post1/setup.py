# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_autoreply']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.0',
 'nonebot2>=2.0.0rc1',
 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-autoreply',
    'version': '0.1.0.post1',
    'description': 'As the name suggests',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# NoneBot-Plugin-AutoReply\n\n_✨ 自动回复 ✨_\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/lgc2333/nonebot-plugin-autoreply.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-autoreply">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-autoreply.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n<a href="https://pypi.python.org/pypi/nonebot-plugin-autoreply">\n    <img src="https://img.shields.io/pypi/dm/nonebot-plugin-autoreply" alt="pypi download">\n</a>\n<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/3eb869b8-2edf-46dd-b325-916d9f8a4888">\n  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/3eb869b8-2edf-46dd-b325-916d9f8a4888.svg" alt="wakatime">\n</a>\n</div>\n\n## 📖 介绍\n\n一个简单的关键词自动回复插件，支持 模糊匹配、完全匹配 与 正则匹配，配置文件高度自定义  \n因为商店里没有我想要的那种关键词回复，所以我就自己写了一个  \n这个插件是从 [ShigureBot](https://github.com/lgc2333/ShigureBot/tree/main/src/plugins/shigure_bot/plugins/keyword_reply) 那边拆出来的，我重写了一下做成了单品插件\n\n插件并没有经过深度测试，如果在使用中遇到任何问题请一定一定要过来发 issue 向我汇报，我会尽快解决  \n如果有功能请求也可以直接发 issue 来 dd 我\n\n## 💿 安装\n\n<details open>\n<summary>[推荐] 使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n```bash\nnb plugin install nonebot-plugin-autoreply\n```\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n```bash\npip install nonebot-plugin-autoreply\n```\n\n</details>\n<details>\n<summary>pdm</summary>\n\n```bash\npdm add nonebot-plugin-autoreply\n```\n\n</details>\n<details>\n<summary>poetry</summary>\n\n```bash\npoetry add nonebot-plugin-autoreply\n```\n\n</details>\n<details>\n<summary>conda</summary>\n\n```bash\nconda install nonebot-plugin-autoreply\n```\n\n</details>\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n```py\nnonebot.load_plugin(\'nonebot_plugin_autoreply\')\n```\n\n</details>\n\n## ⚙️ 配置\n\n插件的配置文件位于 `data/autoreply/replies.json` 下  \n因为把这种东西写在 env 里会太紧凑不易读，所以我单独弄出来了\n\n请根据下面的注释来编辑配置文件，实际配置文件内不要有注释\n\n```jsonc\n[\n  {\n    // 消息的匹配规则，可以放置多个\n    "matches": [\n      {\n        // 用于匹配消息的文本\n        "match": "测试",\n\n        // 匹配模式，可选 `full`(完全匹配)、`fuzzy`(模糊匹配)、`regex`(正则匹配)\n        // 在正则匹配下，请使用 `\\\\` 在 json 里的正则表达式里表示 `\\`，因为 json 解析时本身就会将 `\\` 作为转义字符\n        // 可以不填，默认为 `fuzzy`\n        "type": "fuzzy",\n\n        // 是否需要 at 机器人才能触发（叫机器人昵称也可以）\n        // 可以不填，默认为 `false`\n        "to_me": false,\n\n        // 是否忽略大小写\n        // 可以不填，默认为 `true`\n        "ignore_case": true,\n\n        // 是否去掉消息前后的空格再匹配\n        // 可以不填，默认为 `true`\n        "strip": true,\n\n        // 当带 cq 码的消息匹配失败时，是否使用去掉 cq 码的消息再匹配一遍\n        // 可以不填，默认为 `true`\n        "allow_plaintext": true\n      }\n\n      // 更多匹配规则...\n    ],\n\n    // 匹配成功后，回复的消息\n    // 如果有多个，将随机抽取一个回复\n    "replies": [\n      // 一条使用普通文本形式的消息\n      "这是一条消息，可以使用CQ码[CQ:image,file=https://pixiv.re/103981177.png]",\n\n      // 也可以使用 CQ 码的 json 格式，像这样\n      [\n        {\n          "type": "text",\n          "data": {\n            "text": "也可以使用这种格式"\n          }\n        },\n        {\n          "type": "image",\n          "data": {\n            "file": "https://pixiv.re/103981177.png"\n          }\n        }\n      ]\n\n      // 更多消息...\n    ],\n\n    // 过滤指定群聊\n    // 可以不填，默认为空的黑名单\n    "groups": {\n      // 黑名单类型，可选 `black`(黑名单)、`white`(白名单)\n      "type": "black",\n\n      // 要过滤的群号\n      "values": [\n        123456789, 987654321\n        // 更多群号...\n      ]\n    },\n\n    // 过滤指定用户\n    // 可以不填，默认为空的黑名单\n    "users": {\n      // 黑名单类型，可选 `black`(黑名单)、`white`(白名单)\n      "type": "black",\n\n      // 要过滤的QQ号\n      "values": [\n        1145141919, 9191415411\n        // 更多QQ号...\n      ]\n    }\n  }\n\n  // ...\n]\n```\n\n## 📞 联系\n\nQQ：3076823485  \nTelegram：[@lgc2333](https://t.me/lgc2333)  \n吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  \n邮箱：<lgc2333@126.com>\n\n## 💰 赞助\n\n感谢大家的赞助！你们的赞助将是我继续创作的动力！\n\n- [爱发电](https://afdian.net/@lgc2333)\n- <details>\n    <summary>赞助二维码（点击展开）</summary>\n\n  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)\n\n  </details>\n\n## 📝 更新日志\n\n没有\n',
    'author': 'lgc2333',
    'author_email': 'lgc2333@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
