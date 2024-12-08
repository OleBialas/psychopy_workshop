from argparse import ArgumentParser
from psychopy.sound import Sound
from psychopy.hardware.keyboard import Keyboard
Sound(stereo=False)
kb = Keyboard()

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("step", type=int)
parser.add_argument("n_trials", type=int)
args = parser.parse_args()

freq = args.freq
for i in range(args.n_trials):
    tone = Sound(value=freq, stereo=False)
    tone.play()
    keys = kb.waitKeys(keyList=["up", "down"])
    if keys[0].name == "up":
        freq = freq + args.step
    else:
        freq = freq - args.step