from argparse import ArgumentParser
from psychopy.sound import Sound
from psychopy.visual import Window
from psychopy.event import waitKeys
Sound(stereo=False)

parser = ArgumentParser()
parser.add_argument("frequency", type=int)
parser.add_argument("key", type=str)
parser.add_argument("--timed", action='store_true')
args = parser.parse_args()

with Window() as win:
    tone = Sound(value=args.frequency)
    tone.play()
    keys = waitKeys(keyList=[args.key], timeStamped=args.timed)

    print(keys)