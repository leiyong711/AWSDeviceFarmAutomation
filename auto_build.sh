#!/bin/bash

# 删除 __pycache__ 文件夹
find . -name '__pycache__' -type d -exec rm -r {} +

# 删除 .pyc 文件
find . -name '*.pyc' -exec rm -f {} +

# 删除 .pyo 文件
find . -name '*.pyo' -exec rm -f {} +

# 删除临时文件
find . -name '*~' -exec rm -f {} +

# 压缩文件和文件夹
zip -r test_bundle.zip tests/ requirements.txt
