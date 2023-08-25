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

## 本地测试pytest能否收集到测试用例
```
pytest --collect-only tests
```
#### 有效的 Appium Python 套件應產生輸出如下：
``` 
================================================================================== test session starts ==================================================================================
platform darwin -- Python 3.9.1, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/leiyong/Documents/code3/testing/insta-page-load-automation
collected 1 item                                                                                                                                                                        

<Package tests>
  <Module test_case.py>
    <Class TestAppium>
      <Function test_appium_flow>

=============================================================================== 1 test collected in 0.16s ===============================================================================
```