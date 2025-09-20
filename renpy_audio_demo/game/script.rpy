# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define ai = Character("AI", color="#c8c8ff")
define narrator = Character(None, kind=nvl)

# Initialize Python components
init python:
    # Import required modules for web requests
    try:
        # Python 2
        import urllib2
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
        full_prompt = "
".join(conversation_history) + "
AI:"
        
        # This is just a mock response for demonstration purposes
        mock_responses = [
            "Hello! How can I assist you today?",
            "That's an interesting question. Let me think about it.",
            "I understand what you're asking. Here's my perspective.",
            "Thanks for sharing that with me. What else would you like to discuss?",
            "I'm here to help with any questions you might have.",
            "I appreciate you taking the time to chat with me.",
            "That's a thoughtful point. Let me consider it.",
            "I'm glad you asked about that. Here's what I think:"
        ]
        
        # For now, we'll just return a mock response
        import random
        response_text = random.choice(mock_responses)
        
        # Add AI response to conversation history
        conversation_history.append("AI: " + response_text)
        
        return response_text

# Audio input implementation
init python:
    # Try to import audio libraries
    try:
        import pyaudio
        import wave
        audio_supported = True
    except:
        audio_supported = False
    
    try:
        import speech_recognition as sr
        speech_supported = True
    except:
        speech_supported = False
    
    # Audio recording parameters
    AUDIO_CHUNK = 1024
    AUDIO_FORMAT = pyaudio.paInt16 if audio_supported else None
    AUDIO_CHANNELS = 1
    AUDIO_RATE = 44100
    AUDIO_RECORD_SECONDS = 5
    
    def record_audio_simple(filename="recorded_audio.wav", duration=5):
        """
        Simple audio recording function (requires compatible environment)
        """
        if not audio_supported:
            renpy.notify("Audio recording not supported in this environment")
            return False
            
        try:
            # Initialize PyAudio
            audio = pyaudio.PyAudio()
            
            # Open stream
            stream = audio.open(format=AUDIO_FORMAT,
                                channels=AUDIO_CHANNELS,
                                rate=AUDIO_RATE,
                                input=True,
                                frames_per_buffer=AUDIO_CHUNK)
            
            renpy.notify("Recording for %d seconds..." % duration)
            
            # Record audio
            frames = []
            for i in range(0, int(AUDIO_RATE / AUDIO_CHUNK * duration)):
                data = stream.read(AUDIO_CHUNK)
                frames.append(data)
            
            renpy.notify("Recording finished.")
            
            # Stop and close stream
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
            # Save audio to file
            wf = wave.open(filename, 'wb')
            wf.setnchannels(AUDIO_CHANNELS)
            wf.setsampwidth(audio.get_sample_size(AUDIO_FORMAT))
            wf.setframerate(AUDIO_RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            return True
        except Exception as e:
            renpy.notify("Recording failed: " + str(e))
            return False
    
    def recognize_speech_from_file(filename="recorded_audio.wav"):
        """
        Convert recorded audio to text using speech recognition
        """
        if not speech_supported:
            renpy.notify("Speech recognition not supported in this environment")
            return "Speech recognition not available"
            
        try:
            # Initialize recognizer
            recognizer = sr.Recognizer()
            
            # Load audio file
            with sr.AudioFile(filename) as source:
                audio_data = recognizer.record(source)
            
            # Recognize speech
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)
        except Exception as e:
            return "Speech recognition failed: " + str(e)

# 游戏在此开始。
label start:
    # Show a background
    scene bg room
    
    # Show a character
    show eileen happy
    
    # Display introductory dialogue
    narrator "Welcome to the Ren'Py Audio Input Demo!"
    narrator "This demo shows how to implement audio input functionality in Ren'Py visual novels."
    narrator "You can interact with the AI using either text input or voice commands."
    
    # Initialize conversation history
    $ conversation_history = []
    
    # Enter the chat loop
    call chat_loop

# Chat loop
label chat_loop:
    # Menu for input method selection
    menu:
        "Select input method:"
        "Text input":
            $ user_input = renpy.input("You: ", length=100)
        "Audio input" if audio_supported:
            call screen audio_input_screen
            $ user_input = recognized_text if recognized_text else ""
        "About this demo":
            narrator "This demo shows how to implement audio input in Ren'Py."
            narrator "It uses PyAudio for recording and SpeechRecognition for speech-to-text conversion."
            narrator "For more information, see the documentation files in this project."
            jump chat_loop
        "Exit demo":
            ai "Goodbye! Thanks for trying the audio input demo."
            return
    
    # Check if user wants to exit
    if user_input.lower() == "quit" or user_input.lower() == "exit":
        ai "Goodbye! Thanks for trying the audio input demo."
        return
    
    # Handle empty input
    if user_input.strip() == "":
        if not audio_supported or not recognized_text:
            ai "Please enter a message."
            jump chat_loop
    
    # Call LLM API (using mock function)
    $ ai_response = call_llm_api(user_input)
    
    # Display AI response
    ai "[ai_response]"
    
    # Reset variables for next iteration
    $ recognized_text = ""
    $ processing = False
    
    # Continue chat loop
    jump chat_loop