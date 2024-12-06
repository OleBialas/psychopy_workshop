import argparse
import numpy as np
from psychopy import core, sound
from psychopy.hardware import keyboard

def audiogram(frequency, dur=0.25, start_intensity=1, step=0.1, n_reversals=5):

    kb = keyboard.Keyboard()
    tone = sound.Sound(value=frequency, stereo=False)
    noise = sound.Sound(stereo=False)
    noise.setSoundArr(np.random.randn(48000))
    noise.play(loop=-1)
    reversals=[]
    direction=-1
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
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a pure tone audiogram for a single frequency")
    parser.add_argument("frequency", type=int, help="Frequency of the tone in Hz")
    args = parser.parse_args()
    audiogram(args["frequency"])

