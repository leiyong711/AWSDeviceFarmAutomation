# INSTA 页面加载自动化测试

## 搭建本地虚拟环境
```
1. 安装虚拟环境包
    pip install virtualenv
2. 创建虚拟环境
    virtualenv workspace
3. 激活虚拟环境
    source workspace/bin/activate
```

## 安装依赖包
```
1. 在虚拟环境安装pytest依赖包
    pip install pytest
2. 在虚拟环境中安装 Appium Python 客户端
    pip install Appium-Python-Client
```

## 自动构建AWS Device Farm脚本包
```
sh auto_build.sh
```