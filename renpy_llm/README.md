# Ren'Py 模块化框架

这个项目展示了一个模块化的Ren'Py项目结构，将功能分解为独立的模块，便于维护和扩展。

## 项目结构

```
game/
├── script.rpy                  # 主脚本文件
├── modules/                    # 功能模块
│   ├── ai_client.rpy           # AI客户端
│   ├── audio_input.rpy         # 音频输入
│   ├── chat_system.rpy         # 聊天系统
│   ├── dialogue_system.rpy     # 对话系统
│   ├── game_state.rpy          # 游戏状态管理
│   └── utils.rpy               # 工具函数
├── screens/                    # 屏幕界面
│   └── ui_screens.rpy          # UI屏幕
```

## 模块说明

### 核心模块
- **script.rpy**: 主脚本文件，包含角色定义和游戏入口点
- **modules/chat_system.rpy**: 聊天循环和用户交互逻辑

### 功能模块
- **modules/ai_client.rpy**: DeepSeek API调用封装
- **modules/audio_input.rpy**: 音频录制和语音识别功能
- **modules/dialogue_system.rpy**: 对话历史管理
- **modules/game_state.rpy**: 游戏状态管理
- **modules/utils.rpy**: 通用工具函数

### 屏幕界面
- **screens/ui_screens.rpy**: 用户界面屏幕定义

## 开发指南

1. **添加新功能**: 在`modules/`目录下创建新的模块文件
2. **保持模块独立**: 每个模块应该有明确的职责
3. **使用默认变量**: 使用`default`语句定义全局变量
4. **Python函数**: 在`init python`块中定义Python函数

## 优势

1. **模块化**: 功能分离，便于维护
2. **可扩展**: 易于添加新功能
3. **可重用**: 模块可在不同项目中重用
4. **清晰结构**: 易于理解和协作开发