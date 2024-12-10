from argparse import ArgumentParser
from psychopy.sound import Sound
from psychopy.visual import Window
from psychopy.event import waitKeys
Sound(stereo=False)

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("step", type=int)
parser.add_argument("n_trials", type=int)
args = parser.parse_args()

with Window() as win:
    freq = args.freq
    for i in range(args.n_trials):
        tone = Sound(value=freq, stereo=False)
        tone.play()
        keys = waitKeys(keyList=["up", "down"])
        if keys[0] == "up":
            freq = freq + args.step
        else:
            freq = freq - args.step