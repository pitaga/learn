'''
    配置文件，用于配置options选项和settings等
'''

import os
BASE_DIR = os.path.dirname(__file__)    # 生成当前目录所在的绝对路径


# 参数
options = {
    "port": 8000
}

# 配置
settings = {
    # static_url()方法用于拼接配置的静态，并返回拼接后的路径
    "static_path": os.path.join(BASE_DIR, "static"),
    "template_path": os.path.join(BASE_DIR, "templates"),
    # 设置tornado是否工作在调试模式下，默认为false即工作在生产模式下
    "debug": True,
    # 关闭当前文档的自动转义，不建议使用
    # "aotuescape":None
}