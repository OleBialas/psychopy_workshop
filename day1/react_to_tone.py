from argparse import ArgumentParser
from psychopy.sound import Sound
from psychopy.hardware.keyboard import Keyboard
Sound(stereo=False)
kb = Keyboard()

parser = ArgumentParser()
parser.add_argument("frequency", type=int)
parser.add_argument("key", type=str)
parser.add_argument("--release", action='store_true')
args = parser.parse_args()

tone = Sound(value=args.frequency)
tone.play()
keys = kb.waitKeys(keyList=[args.key], waitRelease=args.release)

print(keys)