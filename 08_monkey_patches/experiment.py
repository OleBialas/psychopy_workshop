from psychopy import core, sound
from psychopy.visual import Window, TextStim
from psychopy.event import waitKeys

cfg = load_config()

def main():
        win = Window()
        text = TextStim(win, text="Press SPACE when you hear a tone!")
        text.draw()
        for i in range(5):
            tone = sound.Sound(secs=1, stereo=False)
            tone.play()
            key = waitKeys(keyList=["space"], timeStamped=True)[0]
            print("Pressed " + key[0] + " after " + str(key[1]) + " secs")
            core.wait(cfg['wait_dur'])
        win.close()

if __name__ == "__main__":
    main()
