# 游戏状态管理模块

# 全局变量
default game_state = {
    "player_name": "玩家",
    "current_chapter": "start",
    "conversation_history": [],
    "inventory": [],
    "settings": {
        "audio_input_enabled": False,
        "subtitles_enabled": True
    }
}

# 更新游戏状态函数
init python:
    def update_game_state(key, value):
        """
        更新游戏状态
        """
        game_state[key] = value
    
    def get_game_state(key, default=None):
        """
        获取游戏状态
        """
        return game_state.get(key, default)
    
    def add_to_inventory(item):
        """
        添加物品到背包
        """
        if item not in game_state["inventory"]:
            game_state["inventory"].append(item)
    
    def remove_from_inventory(item):
        """
        从背包移除物品
        """
        if item in game_state["inventory"]:
            game_state["inventory"].remove(item)