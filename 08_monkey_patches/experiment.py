from psychopy import core, sound
from psychopy.hardware import keyboard


def main():
    kb = keyboard.Keyboard()

    for i in range(5):
        tone = sound.Sound(secs=1, stereo=False)
        tone.play()
        key = kb.waitKeys(keyList=["space"])
        print("Pressed " + key[0].name + " after " + str(key[0].rt) + " secs")
        core.wait(1)


if __name__ == "__main__":
    main()
