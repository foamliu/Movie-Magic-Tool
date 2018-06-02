# Movie Magic 工具

## 架构和选择

用Electron作Python程序的用户界面。前端和后端用`zerorpc`通信。 想了解更多请参考 [electron-python-example](https://github.com/fyears/electron-python-example)。


```text
start
 |
 V
+--------------------+
|                    | start
|  electron          +-------------> +------------------+
|                    | sub process   |                  |
| (browser)          |               | python server    |
|                    |               |                  |
| (all html/css/js)  |               | (business logic) |
|                    |   zerorpc     |                  |
| (node.js runtime,  | <-----------> | (zeromq server)  |
|  zeromq client)    | communication |                  |
|                    |               |                  |
+--------------------+               +------------------+
```

## 依赖项
- [NodeJS](https://nodejs.org/)

以及 Python 的依赖库：
```bash
pip install zerorpc
pip install pyinstaller

# for windows only
pip install pypiwin32 # for pyinstaller
```

## 开始运行

首先执行这条语句来下载、安装项目依赖的包：
```bash
./npm install
```

然后启动 Electron 即可：

```bash
./node_modules/.bin/electron .
```

注意：若在Windows下运行需把上述斜线改成反斜线。
