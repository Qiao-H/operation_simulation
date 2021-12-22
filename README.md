# operation_simulation
# 模拟人看到图片进行鼠标键盘操作的动作

### 目录结构
```
---- main.exe
 |-- config.txt
 |-- img --- image1.png
 |    |----- image2.png
```

### config.txt语法
- 每一行配置的格式：[寻找图片动作]|[图片名字（只可以是英文）]|动作
- "#"开头的行和空行会被忽略，其他行会被识别并从上往下执行
- 例如：
- 1. "edge.png|enter"表示找到edge.png后按enter键
- 2. "edge.png|~l"表示找到edge.png后按鼠标左键
- 2. "|down"表示按方向键下
- 3. "down|edge.png|~l"表示按方向下键直到找到edge.png，然后按鼠标左键

### 一些常用按键
- "enter": 按enter键
- "backspace"：按退格键
- "~l"：鼠标左键
- "~r"：鼠标右键
- "~dl"：左键双击
- "abcdefg"：键盘输入abcdefg


### 举例
- 去b站打开国王排名（下面内容即为config.txt里面配置的内容）
```
# 键盘按左侧win键
|winleft
# 找到edge.png并点击鼠标左键（打开edge浏览器）
edge.png|~l
# 找到window_head.png并左键双击（最大化浏览器）
window_head.png|~dl
# 找到url.png并鼠标左键点击，接着输入bilibili.com，并按两下enter键
url.png|~l,bilibili.com,enter,enter
# 按键盘下方向键直到找到guowangpaiming.png，找到后鼠标左键点击
down|guowangpaiming.png|~l
```