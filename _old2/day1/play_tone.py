from argparse import ArgumentParser
import time
from psychopy.sound import Sound
Sound(stereo=False)

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("secs", type=float)
args = parser.parse_args()

tone = Sound(value=args.freq, secs=args.secs, stereo=False)
tone.play()
time.sleep(args.secs)
