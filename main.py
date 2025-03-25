import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 

name = ""
seconds = int(input("Choose the length of the recording in seconds:"))


print("Recording...")

record_voice = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()

print("What you want to call your recording?")
name = input()
write(f"{name}.wav", fs, record_voice)
print("Done!")
