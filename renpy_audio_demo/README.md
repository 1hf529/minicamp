# Ren'Py Audio Input Demo

This project demonstrates how to implement audio input functionality in Ren'Py visual novels. It allows users to interact with the game using voice commands in addition to traditional text input.

## Features

- Audio recording from microphone
- Speech-to-text conversion
- User-friendly interface for audio input
- Fallback to text input when audio is not supported
- Error handling and user feedback
- Cross-platform compatibility

## Project Structure

```
renpy_audio_demo/
├── game/
│   ├── script.rpy          # Main game script with audio functionality
│   ├── screens.rpy         # Custom screens for UI
│   ├── options.rpy         # Game options
│   ├── gui.rpy             # GUI configuration
│   ├── images/             # Image assets
│   ├── audio/              # Audio assets
│   └── python-packages/    # Python libraries (if needed)
├── README.md               # This file
└── LICENSE                 # License information
```

## Requirements

- Ren'Py 7.4 or higher
- Python 3.7 or higher
- PyAudio library (for audio recording)
- SpeechRecognition library (for speech-to-text)

## Installation

1. Install Ren'Py from https://www.renpy.org/
2. Create a new project in Ren'Py
3. Replace the default files with the files from this repository
4. Install required Python packages:
   ```
   pip install pyaudio speechrecognition
   ```

## Usage

1. Launch the game in Ren'Py
2. At the main menu, select "Audio Input Demo"
3. Choose between text input and audio input
4. For audio input:
   - Click "Record Audio" to start recording
   - Speak into your microphone
   - Click "Process Audio" to convert speech to text
   - Review the recognized text and confirm or edit
5. The AI will respond to your input

## Implementation Details

### Audio Recording

The audio recording functionality uses PyAudio to capture audio from the microphone. The implementation includes:

- Configuration of audio parameters (sample rate, channels, format)
- Real-time audio capture with progress feedback
- Saving recorded audio to WAV files
- Error handling for recording failures

### Speech Recognition

Speech recognition is implemented using the SpeechRecognition library. Features include:

- Support for multiple speech recognition engines
- Automatic language detection
- Error handling for recognition failures
- Fallback mechanisms for network issues

### User Interface

The UI provides:

- Clear visual feedback during recording
- Simple controls for recording and processing
- Display of recognized text
- Error messages and status updates
- Graceful fallback to text input

## Platform Considerations

### Windows

- PyAudio usually works out of the box
- May require Visual Studio build tools

### macOS

- May require PortAudio installation:
  ```
  brew install portaudio
  pip install pyaudio
  ```

### Linux

- Requires system packages:
  ```
  sudo apt-get install portaudio19-dev python3-pyaudio
  pip install pyaudio
  ```

## Limitations

- Audio libraries may not work in Ren'Py's sandboxed environment
- Speech recognition requires internet connectivity for Google API
- Performance may be affected on slower systems
- Mobile platforms not supported in standard Ren'Py builds

## Extending the Demo

To add real LLM integration:

1. Replace the mock `call_llm_api` function with actual API calls
2. Add your API key and endpoint information
3. Implement proper error handling for network requests
4. Add conversation history management

## License

This project is licensed under the MIT License - see the LICENSE file for details.