# 音频输入模块

init python:
    # 尝试导入音频库
    try:
        import pyaudio
        import wave
        audio_supported = True
    except Exception as e:
        audio_supported = False
        print("Audio recording not supported: " + str(e))
    
    try:
        import speech_recognition as sr
        speech_supported = True
    except Exception as e:
        speech_supported = False
        print("Speech recognition not supported: " + str(e))
    
    # 音频录制参数
    AUDIO_CHUNK = 1024
    AUDIO_FORMAT = pyaudio.paInt16 if audio_supported else None
    AUDIO_CHANNELS = 1
    AUDIO_RATE = 44100
    AUDIO_RECORD_SECONDS = 5
    
    def record_audio_simple(filename="recorded_audio.wav", duration=5):
        """
        简单音频录制功能（需要兼容的环境）
        """
        if not audio_supported:
            renpy.notify("Audio recording not supported in this environment")
            return False
            
        try:
            # 初始化PyAudio
            audio = pyaudio.PyAudio()
            
            # 打开流
            stream = audio.open(format=AUDIO_FORMAT,
                                channels=AUDIO_CHANNELS,
                                rate=AUDIO_RATE,
                                input=True,
                                frames_per_buffer=AUDIO_CHUNK)
            
            renpy.notify("Recording for %d seconds..." % duration)
            
            # 录制音频
            frames = []
            for i in range(0, int(AUDIO_RATE / AUDIO_CHUNK * duration)):
                data = stream.read(AUDIO_CHUNK)
                frames.append(data)
            
            renpy.notify("Recording finished.")
            
            # 停止并关闭流
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
            # 保存音频到文件
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
        将录制的音频转换为文本
        """
        if not speech_supported:
            renpy.notify("Speech recognition not supported in this environment")
            return "Speech recognition not available"
            
        try:
            # 初始化识别器
            recognizer = sr.Recognizer()
            
            # 加载音频文件
            with sr.AudioFile(filename) as source:
                audio_data = recognizer.record(source)
            
            # 识别语音
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)
        except Exception as e:
            return "Speech recognition failed: " + str(e)

# 音频输入屏幕
screen audio_input_screen():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        vbox:
            spacing 20
            
            text "Audio Input" size 24
            
            if audio_supported and speech_supported:
                textbutton "Record Audio (5 seconds)" action Function(record_audio_simple, "user_recording.wav", 5)
                
                if renpy.exists("user_recording.wav"):
                    text "Recording ready for processing"
                    textbutton "Process Audio" action [SetVariable("processing", True), 
                        SetVariable("recognized_text", recognize_speech_from_file("user_recording.wav"))]
                
                if processing:
                    if recognized_text:
                        text "Recognized Text:" size 18
                        text recognized_text
                    else:
                        text "Processing audio..."
            else:
                if not audio_supported:
                    text "Audio recording is not supported in this environment."
                if not speech_supported:
                    text "Speech recognition is not supported in this environment."
                text "Please use text input instead."
            
            textbutton "Back" action Return()