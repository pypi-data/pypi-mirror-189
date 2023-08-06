# etcdproxy

提供etcd的代理对象功能.本项目代理的对象是

+ aio模式代理[aetcd](https://aetcd.readthedocs.io/en/latest/index.html)
+ 普通模式代理[etcd3](https://python-etcd3.readthedocs.io/en/latest/)

需要注意这两个模块本身冲突,也就是说如果`import etcd3`就不能再`import aetcd`.因此同一个程序中不能混用两种模式.如果并不确定使用的是什么模式可以在代理的`aio`字段进行确认

## 安装

```bash
pip install etcdproxy
```
