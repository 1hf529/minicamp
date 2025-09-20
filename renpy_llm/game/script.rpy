# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define e = Character("艾琳")
define ai = Character("AI")

init python:
    import json
    import urllib.request as urllib2
    import urllib.error as urllib_error
    import ssl
    import os
    
    # Function to get API key from config file
    def get_api_key():
        try:
            # Try to read from config file
            with open("game/config.txt", "r") as f:
                for line in f:
                    if line.startswith("DEEPSEEK_API_KEY="):
                        return line.split("=", 1)[1].strip()
        except:
            pass
        # Fallback to environment variable
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if api_key:
            return api_key
        return ""
    
    # Function to call DeepSeek API
    def call_deepseek_api(prompt, conversation_history):
        """
        Call DeepSeek API to get AI response
        """
        try:
            # Prepare the API request
            url = "https://api.deepseek.com/v1/chat/completions"
            api_key = get_api_key()
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + api_key
            }
            
            # Prepare the conversation history
            messages = []
            # Add system message
            messages.append({"role": "system", "content": "You are a helpful AI assistant."})
            
            # Add conversation history
            for entry in conversation_history:
                if entry.startswith("User: "):
                    messages.append({"role": "user", "content": entry[6:]})
                elif entry.startswith("AI: "):
                    messages.append({"role": "assistant", "content": entry[5:]})
            
            # Add the current user prompt
            messages.append({"role": "user", "content": prompt})
            
            # Prepare the data
            data = {
                "model": "deepseek-chat",
                "messages": messages,
                "max_tokens": 500,
                "temperature": 0.7
            }
            
            # Convert to JSON
            json_data = json.dumps(data).encode('utf-8')
            
            # Create SSL context that doesn't verify certificates (for testing)
            # Note: In production, you should properly configure certificates
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            # Create request
            req = urllib2.Request(url, json_data, headers)
            
            # Send request with SSL context
            response = urllib2.urlopen(req, context=context)
            
            # Read response
            response_data = response.read().decode('utf-8')
            
            # Parse JSON
            response_json = json.loads(response_data)
            
            # Extract the response text
            response_text = response_json["choices"][0]["message"]["content"]
            
            return response_text
            
        except Exception as e:
            # Fallback to mock response if API fails
            print("DeepSeek API call failed: " + str(e))
            return "抱歉，我暂时无法回答您的问题。请稍后再试。"

label start:
    e "您已创建了一个新的 Ren'Py 游戏。"
    e "现在我们将演示如何与AI进行对话。"
    
    # Initialize conversation history
    $ conversation_history = []
    
    # Enter chat loop
    call chat_loop

label chat_loop:
    # Get user input
    $ user_input = renpy.input("您: ", length=100)
    
    # Check if user wants to exit
    if user_input.lower() == "quit" or user_input.lower() == "exit":
        ai "再见！感谢与我聊天。"
        return
    
    # Handle empty input
    if user_input.strip() == "":
        ai "请输入一条消息。"
        jump chat_loop
    
    # Call DeepSeek API
    $ ai_response = call_deepseek_api(user_input, conversation_history)
    
    # Add to conversation history
    $ conversation_history.append("User: " + user_input)
    $ conversation_history.append("AI: " + ai_response)
    
    # Display AI response
    ai "[ai_response]"
    
    # Continue chat loop
    jump chat_loop