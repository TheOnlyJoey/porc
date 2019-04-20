import sounddevice as sd

def capture_audio(duration)
	sd.default.samplerate = 48000
	sd.default.channels = 2
	captured_stream = sd.rec(int(duration * 48000), samplerate=48000, channels=2)
	return captured_stream

def playback_audio(stream)
	sd.play(stream, 48000)
	return True

def playback_stop(stream)
	sd.stop()
	return True