# 对话系统模块

# 对话系统函数
init python:
    def add_to_conversation_history(role, message):
        """
        添加消息到对话历史
        """
        conversation_history.append(f"{role}: {message}")
        
    def get_recent_conversation_context(count=5):
        """
        获取最近的对话上下文
        """
        return "\n".join(conversation_history[-count:]) if conversation_history else ""