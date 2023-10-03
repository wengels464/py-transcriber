import sys
import speech_recognition as sr

# Check if a filename argument was provided
if len(sys.argv) < 2:
    print("Usage: python transcribe.py <audio_file>")
    sys.exit(1)

# Get the audio file path from the command line argument
audio_file = sys.argv[1]

# Initialize the recognizer
recognizer = sr.Recognizer()

# Open and recognize the audio file
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)

# Transcribe the audio
transcript = recognizer.recognize_google(audio)

# Print or use the transcript as needed
print("Transcript:")
print(transcript)