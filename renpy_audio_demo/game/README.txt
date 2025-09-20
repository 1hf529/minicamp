# Ren'Py Audio Input Demo

This demo project shows how to implement audio input functionality in Ren'Py visual novels. Users can interact with the AI using either text input or voice commands.

## Features Demonstrated

1. Audio recording from microphone
2. Speech-to-text conversion
3. User interface for audio input
4. Fallback to text input when audio is not supported
5. Error handling and user feedback

## How to Use This Demo

1. Launch the game in Ren'Py
2. At the main menu, select "Audio Input Demo"
3. Choose between text input and audio input
4. For audio input:
   - Click "Record Audio" to start recording
   - Speak into your microphone
   - Click "Process Audio" to convert speech to text
   - Review the recognized text and confirm or edit
5. The AI will respond to your input

## Technical Implementation

The demo uses:
- PyAudio for audio recording
- SpeechRecognition library for speech-to-text conversion
- Custom Ren'Py screens for the user interface

## Platform Support

- Windows: Full support with proper library installation
- macOS: Requires PortAudio installation
- Linux: Requires system audio development packages
- Mobile: Not supported in standard Ren'Py builds
- Web: Not supported in web deployments

## Extending the Demo

To connect to a real LLM API:
1. Replace the mock `call_llm_api` function with actual API calls
2. Add your API key and endpoint information
3. Implement proper error handling for network requests
4. Add conversation history management

This demo provides a foundation that can be extended for more sophisticated audio input capabilities.