# 工具函数模块

init python:
    import os
    import hashlib
    import json
    
    def generate_hash(data):
        """
        生成数据的MD5哈希值
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.md5(data).hexdigest()
    
    def safe_file_read(filepath):
        """
        安全读取文件
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return None
    
    def safe_file_write(filepath, content):
        """
        安全写入文件
        """
        try:
            # 确保目录存在
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error writing file {filepath}: {e}")
            return False
    
    def format_elapsed_time(seconds):
        """
        格式化经过的时间
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"