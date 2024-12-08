from argparse import ArgumentParser
from psychopy.sound import Sound
from psychopy.hardware.keyboard import Keyboard
Sound(stereo=False)
kb = Keyboard()

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("key", type=str)
parser.add_argument("n_trials", type=int)
args = parser.parse_args()

for i in range(args.n_trials):
    tone = Sound(value=args.freq)
    tone.play()
    keys = kb.waitKeys(keyList=[args.key])
    print(keys)