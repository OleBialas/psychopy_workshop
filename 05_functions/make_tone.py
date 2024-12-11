from psychopy.sound import Sound

def make_tone(frequency=300, duration=0.3):
    return Sound(value=frequency, secs=duration)