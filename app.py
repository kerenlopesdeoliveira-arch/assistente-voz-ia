import sounddevice as sd
from scipy.io.wavfile import write
from openai import OpenAI
from gtts import gTTS
import os

client = OpenAI(api_key="client = OpenAI(api_key="SUA_API_KEY_AQUI")")

# Gravar áudio
fs = 44100
seconds = 5

print("Fale agora...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("audio.wav", fs, audio)

# Transcrever áudio
audio_file = open("audio.wav", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe",
    file=audio_file
)

texto = transcription.text
print("Você disse:", texto)

# ChatGPT responde
resposta = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": texto}]
)

texto_resposta = resposta.choices[0].message.content
print("Resposta:", texto_resposta)

# Converter em voz
tts = gTTS(text=texto_resposta, lang='pt')
tts.save("resposta.mp3")

os.system("start resposta.mp3")