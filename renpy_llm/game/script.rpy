# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define e = Character("艾琳")
define ai = Character("AI")

# 导入模块
init python:
    import sys
    import os
    
    # 将modules目录添加到Python路径
    modules_dir = os.path.join(config.gamedir, "modules")
    if modules_dir not in sys.path:
        sys.path.append(modules_dir)

# 全局变量
default conversation_history = []
default audio_supported = False
default speech_supported = False
default processing = False
default recognized_text = ""

# 游戏在此开始。
label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。
    show eileen happy

    # 此处显示各行对话。
    e "您已创建了一个新的 Ren'Py 游戏。"
    e "现在我们将演示如何与AI进行对话。"

    # 初始化对话历史
    $ conversation_history = []

    # 进入对话循环
    call chat_loop from _call_chat_loop