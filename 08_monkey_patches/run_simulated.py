import random
from unittest.mock import Mock, patch
from experiment import main

def beep():
    print("beep")

def wait(t):
    print("Waiting for " + str(t))

def randomKey(keyList, timeStamped):
    """Pick a random key from the key list and return KeyPress object with random reaction time"""
    rt = random.random()
    name = random.choice(keyList)
    if timeStamped:
        return [[name, rt]]
    else:
        return [name]


with (
    patch("experiment.Window"),
    patch("experiment.TextStim"),
    patch("experiment.sound.Sound.play", side_effect=beep),
    patch("experiment.core.wait", side_effect=wait),
    patch("experiment.waitKeys", side_effect=randomKey),
):
    # kb.waitKeys.return_value = randomKey
    main()
