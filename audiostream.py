import sounddevice as sd
import numpy as np
from ir import *

def capture_audio(duration):
	sd.default.samplerate = 48000
	sd.default.channels = 2
	captured_stream = sd.rec(int(duration * 48000), samplerate=48000, channels=2)
	return captured_stream

def playback_audio(stream):
	sd.play(stream, 48000)
	return True

def playback_stop(stream):
	sd.stop()
	return True

def generate_sinewave(duration):
	# sine frequency in Hz
	f = 440.0
	samples = (np.sin(2*np.pi*np.arange(48000*duration)*f/48000)).astype(np.float32)
	return samples

def generate_sweeps(duration):
	ess, inv = generate_ess(duration, 20, 20000)
	return (ess,inv)