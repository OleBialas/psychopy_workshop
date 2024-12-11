from psychopy.sound import Sound

def make_tone(frequency=300, duration=0.3):
    return Sound(value=frequency, secs=duration)

def make_and_play_tone(frequency=300, duration=0.3, play=False):
    tone = Sound(value=frequency, secs=duration)
    if play:
        tone.play()
    return tone