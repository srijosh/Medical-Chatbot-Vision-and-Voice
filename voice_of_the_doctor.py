import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from dotenv import load_dotenv
from pydub import AudioSegment
load_dotenv()



#Use Model for Text output to Voice output


#Step1a: Setup Text to Speech–TTS–model with gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    wav_filepath = "final.wav"

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(wav_filepath, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    return output_filepath

# input_text="Hi this is Srijan Joshi from Nepal. I am learning AI. I am testing the text to speech model with gTTS."
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")



#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    wav_filepath = "final.wav"

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(wav_filepath, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath]) 
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
        
    return output_filepath

#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing.mp3")