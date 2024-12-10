import random
from unittest.mock import Mock, patch
from experiment import main


def beep():
    print("beep")


def wait(t):
    print("Waiting for " + str(t))


def randomKey(keyList):
    """Pick a random key from the key list and return KeyPress object with random reaction time"""
    key = Mock()
    key.rt = random.random()
    key.name = random.choice(keyList)
    return [key]


kb = Mock()
kb.waitKeys = randomKey

with (
    patch("experiment.sound.Sound.play", return_value=beep),
    patch("experiment.core.wait", return_value=wait),
    patch("experiment.keyboard.Keyboard", return_value=kb),
):
    # kb.waitKeys.return_value = randomKey
    main()
