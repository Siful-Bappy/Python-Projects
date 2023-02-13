### pip install sounddevice
### pip install scipy
### https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide

import sounddevice
from scipy.io.wavfile import write
fs = 44100
second = 10
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels = 2)
sounddevice.wait()
write("D:output.wav", fs, record_voice)