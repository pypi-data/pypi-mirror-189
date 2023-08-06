# a13e

一个简单且可扩展的听歌识曲包，目前仅支持网易云音乐chromium插件API

## 快速使用
```shell
pip install a13e
a13e -h
```

## 作为python模块使用
```python
from pathlib import Path
import a13e

audio_fp = Path('aaa.mp3')
a13e.recognize(audio_fp) #调用所有的识别器并返回结果

result = a13e.random_recognize(audio_fp) # 调用所有的识别器并随机返回一个结果
a13e.set_tag(audio_fp, result) # 将返回的结果设置为MP3标签
```

## 编写识别器
```
myproject
│  main.py #程序入口
│
└─plugins
        __init__.py #必须
        new_recognizer.py
```
```python
#myproject/main.py
from importlib import import_module
from a13e.plugin import PluginRegister

PluginRegister(import_module('plugins'))
```
```python
#myproject/plugins/new_recognizer.py
from a13e.plugin import PluginRegister
from a13e.recognizer import BaseRecognizer

@PluginRegister.register
class NewRecognizer(BaseRecognizer):
    ...
```

## 目前支持的平台
| 平台    | 识别器名称               | 额外参数 | 描述                                                                                                                                            |
|-------|---------------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 网易云音乐 | `NeteaseCloudMusic` | 没有   | 本API来自[网易云音乐听歌识曲插件](https://chrome.google.com/webstore/detail/%E4%BA%91%E9%9F%B3%E4%B9%90%E5%90%AC%E6%AD%8C/kemcalcncfhmdkgglekijclbomdoohkp) |

## 参考
<https://github.com/akinazuki/NeteaseCloudMusic-Audio-Recognize>
