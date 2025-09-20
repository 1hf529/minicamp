# AI客户端模块

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