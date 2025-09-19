# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define e = Character("艾琳")
define ai = Character("AI")

init python:
    # Import required modules
    try:
        # Python 2
        import urllib2
        import json
    except ImportError:
        # Python 3
        import urllib.request as urllib2
        import urllib.error as urllib_error
        import json
    
    # Global variable to store conversation history
    conversation_history = []
    
    # Function to call LLM API
    def call_llm_api(prompt):
        """
        This is a placeholder function for calling an LLM API.
        In a real implementation, you would replace this with actual API calls.
        """
        # Add user prompt to conversation history
        conversation_history.append("User: " + prompt)
        
        # Build the full prompt with conversation history
        full_prompt = "\n".join(conversation_history) + "\nAI:"
        
        # In a real implementation, you would do something like:
        # For Python 2:
        # url = "https://api.example.com/llm"  # Replace with actual API endpoint
        # data = json.dumps({
        #     "prompt": full_prompt,
        #     "max_tokens": 150,
        #     "temperature": 0.7
        # })
        # req = urllib2.Request(url, data, {
        #     'Content-Type': 'application/json',
        #     'Authorization': 'Bearer YOUR_API_KEY'  # Replace with actual API key
        # })
        # response = urllib2.urlopen(req)
        # result = json.loads(response.read())
        # response_text = result["response"]
        #
        # For Python 3:
        # import urllib.request
        # import urllib.error
        # url = "https://api.example.com/llm"  # Replace with actual API endpoint
        # data = json.dumps({
        #     "prompt": full_prompt,
        #     "max_tokens": 150,
        #     "temperature": 0.7
        # }).encode('utf-8')
        # req = urllib.request.Request(url, data, {
        #     'Content-Type': 'application/json',
        #     'Authorization': 'Bearer YOUR_API_KEY'  # Replace with actual API key
        # })
        # try:
        #     response = urllib.request.urlopen(req)
        #     result = json.loads(response.read().decode('utf-8'))
        #     response_text = result["response"]
        # except urllib.error.URLError as e:
        #     response_text = "Error connecting to API: " + str(e)
        
        # This is just a mock response for demonstration purposes
        mock_responses = [
            "Hello! How can I assist you today?",
            "That's an interesting question. Let me think about it.",
            "I understand what you're asking. Here's my perspective.",
            "Thanks for sharing that with me. What else would you like to discuss?",
            "I'm here to help with any questions you might have."
        ]
        
        # For now, we'll just return a mock response
        import random
        response_text = random.choice(mock_responses)
        
        # Add AI response to conversation history
        conversation_history.append("AI: " + response_text)
        
        return response_text

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
    
    # 调用LLM API（使用模拟函数）
    $ ai_response = call_llm_api(user_input)
    
    # 显示AI响应
    ai "[ai_response]"
    
    # 继续对话循环
    jump chat_loop