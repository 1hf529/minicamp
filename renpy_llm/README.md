# Ren'Py LLM Integration Demo

This project demonstrates how to integrate LLM chat functionality with Ren'Py, creating a text-based conversational interface within a visual novel framework.

## Project Structure

- `game/script.rpy` - Main game script with LLM integration
- `README.md` - This file

## Features Implemented

- Character-based dialogue system using Ren'Py's native interface
- Text input for user prompts with Ren'Py's built-in input system
- Simulated LLM responses (mock implementation)
- Conversation history tracking
- Exit commands ("quit" or "exit")

## How to Run

1. Install Ren'Py from https://www.renpy.org/
2. Open Ren'Py and launch the project
3. Run the game to test the chat functionality

## LLM Integration

The current implementation uses a mock function to simulate LLM responses. To connect to a real LLM API:

1. Replace the `call_llm_api` function in `game/script.rpy` with actual API calls
2. Add your API key and endpoint information
3. Ensure proper error handling for network requests

Example API integration code is included in the comments of the `call_llm_api` function.

## Next Steps

- Integrate with a real LLM API (OpenAI GPT, Claude, etc.)
- Implement conversation history context in API calls
- Add support for multiple characters with different personalities
- Create a more sophisticated UI for the chat interface
- Add support for other input modalities (voice, image)