import argparse
import numpy as np
from psychopy import core, sound
from psychopy.hardware import keyboard

###  define param

### pasrse command line arguments ###
parser = argparse.ArgumentParser()
parser.add_argument("frequency", type=int, help="Frequency of the tone in Hz")
parser = argparse.ArgumentParser(description="Run a pure tone audiogram for a single frequency")
args = parser.parse_args()

kb = keyboard.Keyboard(tone = sound.Sound(value=args.frequency, stereo=False)
noise = sound.Sound(stereo=False)
noise.setSoundArr(np.random.randn(48000)))

tone = sound.Sound(value=args.frequency, stereo=False)
noise = sound.Sound(stereo=False)
noise.setSoundArr(np.random.randn(48000))

reversals=[]
direction=-1  # directon of the staircae
noise.play(loop=-1)
while len(reversals) < n_reversals:
    core.wait(np.random.randint(500, 2000)/1000)
    tone.play()
    keys = kb.waitKeys(keyList=['space'], maxWait=1)
    if len(keys) == 0:
        ... # increase level
        if direction == -1:
            direction = 1
            reversals.append() # append current level
    else:
        ... #decrease level
        if direction == 1:
            direction = -1
            reversals.append() # append current level
print(f"The detection threshold for {frequency} Hz is {np.mean(reversals)}")
        


