from argparse import ArgumentParser
from psychopy.sound import Sound
from psychopy.visual import Window
from psychopy.event import waitKeys
Sound(stereo=False)

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("key", type=str)
parser.add_argument("n_trials", type=int)
args = parser.parse_args()

with Window() as win:
    for i in range(args.n_trials):
        tone = Sound(value=args.freq)
        tone.play()
        keys = waitKeys(keyList=[args.key])
        print(keys)