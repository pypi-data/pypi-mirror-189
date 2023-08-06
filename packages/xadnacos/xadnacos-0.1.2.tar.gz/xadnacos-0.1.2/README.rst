========
xadnacos
========


.. image:: https://img.shields.io/pypi/v/xadnacos.svg
        :target: https://pypi.python.org/pypi/xadnacos

.. image:: https://img.shields.io/travis/KONE-XAD/xadnacos.svg
        :target: https://travis-ci.org/KONE-XAD/xadnacos

.. image:: https://readthedocs.org/projects/xadnacos/badge/?version=latest
        :target: https://xadnacos.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


xadnacos是一个用来调用naccos的sdk

参考https://github.com/KcangYan/nacos-python-sdk.git进行了修改


* Free software: MIT license


文档
--------
导入dkimageapp库::

    from xadnacos import xadnacos as nacos

创建nacos连接对象::

    nacosServer = nacos.nacos(ip=nacosIp,port=nacosPort)

将本地配置注入到nacos对象中即可获取远程配置::

    GlobalConfig={}
    nacosServer.config(dataId="demo-python.json",group="dev",tenant="python",myConfig=GlobalConfig)

注册nacos服务::
   
    serverHost = socket.gethostbyname(socket.gethostname())
    metadata = {
        "tier": "backend",
        "projectid": "THID89782455-HJ45678963"
    }
    clusterName = myConfig.region
    
    nacosServer.registerService(serviceIp=serverHost,servicePort=myConfig.port,serviceName="python-provider",
                                namespaceId="python",groupName="dev",clusterName=clusterName,metadata=metadata)

开启监听配置线程和服务注册心跳进程的健康检查进程::

    nacosServer.healthyCheck()




Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
