# superagent-demo

一个演示用的 Python 命令行小工具：`add.py` 接收两个数字，输出它们的和。

## 功能

- 接收两个数字参数 `A`、`B`，输出 `A + B`
- 同时支持整数和浮点数
- 使用十进制精确计算，`0.1 + 0.2` 会输出 `0.3`
- 参数缺失或不是数字时，打印错误提示并以非零状态码退出

## 环境要求

- Python 3.8 或更高版本
- 无第三方依赖

## 运行示例

整数相加：

```bash
$ python add.py 2 3
5
```

浮点数相加：

```bash
$ python add.py 1.5 2.25
3.75
```

整数与浮点数混合：

```bash
$ python add.py 1 0.5
1.5
```

负数：

```bash
$ python add.py -4 1.5
-2.5
```

查看帮助：

```bash
$ python add.py --help
usage: add.py [-h] A B
...
```

## 运行测试

在仓库根目录执行：

```bash
python -m unittest -v
```
