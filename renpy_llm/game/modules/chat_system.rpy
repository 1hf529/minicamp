# 聊天系统模块

# Chat loop
label chat_loop:
    # 获取用户输入
    $ user_input = renpy.input("您: ", length=100)

    # 检查用户是否想要退出
    if user_input.lower() == "quit" or user_input.lower() == "exit":
        ai "再见！感谢与我聊天。"
        return

    # 处理空输入
    if user_input.strip() == "":
        ai "请输入一条消息。"
        jump chat_loop

    # 调用AI API（使用模拟函数）
    $ ai_response = call_deepseek_api(user_input, conversation_history)

    # 添加到对话历史
    $ conversation_history.append("User: " + user_input)
    $ conversation_history.append("AI: " + ai_response)

    # 显示AI响应
    ai "[ai_response]"

    # 继续对话循环
    jump chat_loop