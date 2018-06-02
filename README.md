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

## 开始运行

运行这个试试看：

```bash
./node_modules/.bin/electron .
```

Awesome!

If something like dynamic linking errors shows up, try to clean the caches and install the libraries again.

```bash
rm -rf node_modules
rm -rf ~/.node-gyp ~/.electron-gyp

npm install
```
