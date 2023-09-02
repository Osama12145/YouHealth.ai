
import assemblyai as aai

aai.settings.api_key = "446983819e4548189bab40f2c5c3a5b9"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("harvard.wav",
config = aai.TranscriptionConfig(summarization=True))


print(transcript.summary)