# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()




import elevenlabs
from elevenlabs.client import ElevenLabs
import os
from gtts import gTTS
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    # Verify the file exists
    if not os.path.exists(output_filepath):
        raise FileNotFoundError(f"Audio file not found: {output_filepath}")

    # Play the audio file using pydub
    audio_segment = AudioSegment.from_file(output_filepath, format="mp3")
    play(audio_segment)

#testing
#input_text="Hi this is Vivek, autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath=r"testing_audios/gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    load_dotenv()
    ELEVENLABS_API_KEY= os.getenv("ELEVENLABS_API_KEY") 
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    # Verify the file exists
    if not os.path.exists(output_filepath):
        raise FileNotFoundError(f"Audio file not found: {output_filepath}")

    # Play the audio file using pydub
    audio_segment = AudioSegment.from_file(output_filepath, format="mp3")
    play(audio_segment)

#testing
#input_text="Hi this is Vivek, autoplay testing!"
#text_to_speech_with_elevenlabs(input_text, output_filepath=r"testing_audios/elevenlabs_testing_autoplay.mp3")