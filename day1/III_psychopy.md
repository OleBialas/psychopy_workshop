# PsychoPy


## 1. Getting responses

```python
from psychopy import core, event
```

### Reference Table
| Code                                       | Description                                                               |
| ---                                        | ---                                                                       |
| `clock = core.Clock()`                     | Initialize a clock to keep time                                           |
| `clock.reset()`                            | Reset the timer to zero                                                   |
| `keys = event.getKeys(keyList=["O", "K"])` | Return a list of all pressed keys that appear in `keyList`                |
| `keys = event.waitKeys(maxWait=5)`         | Wait until a key was pressed or `maxWait` passed                          |
| `keys = event.waitKeys(timeStamped=clock)` | Use an instance of `Clock` to time stamp the keypress                     |

### Key Exercises
1. Write a script that records keys within a certain interval and prints out their names
2. Write a script that waits for a key press and returns the response time


## 2. Visual Display

```python
from psychpopy import visual
```

### Reference Table
| Code                                                            | Description                                                   |
| ---                                                             | ---                                                           |
| `win = visual.Window(size=(800,600))`                           | Create an Window that is 800x600 pixels                       |
| `win.flip()`                                                    | Clear the screen and display new image                        |
| `win.close()`                                                   | Close the Window (usually at the end of the experiment)       |
| `text = visual.textstim(win, text="hi!")`                       | Create a text object for the given `Window`                   |
| `rect = visual.Rect(win, width=1, height=1, lineColor="white")` | Create a rectangle for the given `Window`                     |
| `rect.draw()`                                                   | Draw a visual stimulus (e.g. rectangle) to the buffer         |

### Key Exercises
1. Create a PsychoPy window, wait for a key press and close it again
2. Draw a rectangle with text inside and display them on the screen


## 3. Experimental timing

```python
from psychopy import core, visual
```

### Reference Table
| Code                                           | Description                                       |
| ---                                            | ---                                               |
| `win = visual.Window(fullscr=True)`            | Create a full screen window                       |
| `win.getActualFrameRate()`                     | Measure your screen's frame rate                  |
| `img = visual.ImageStim(win, image="pic.png")` | Load an image and attach it to the given `Window` |
| `img.draw()`                                   | Measure your screen's frame rate                  |
| `clock = core.Clock()`                         | Initialize the timer                              |
| `t = clock.getTime()`                          | Get a time stamp from the clock.                  |
| `core.wait(0.5)`                               | Pause for a given time (in seconds)               |

### Key Exercises

1. Get frame rate and calculate possible duration for visual stimuli
2. Correct clock for the time it takes to load an image


## 4. Playing sounds

```python
import numpy as np
from psychopy import sound
import psychtoolbox as ptb
```

| Code                                | Description                                           |
| ---                                 | ---                                                   |
| `tone = sound.Sound("A", secs=0.5)` | Generate an A note that lasts 500 ms                  |
| `tone.play(loop=3)`                 | Play the sound and repeat it in a loop                |
| `tone.stop`                         | Stop the playback of the sound                        |
| `tone.sndArray`                     | Attribute containing the sound values                 |
| `tone.setSound(x)`                  | Replace the content of `.sndArray` with the array `x` |
| `now = ptb.GetSecs()`               | Get time stamp from the PsychToolBox clock            |
| `tone.play(when=now+0.5)`           | Schedule sound to play exactly 500 ms from now        |

### Key Exercises
1. Generate and play a tone with white noise in the background
2. Schedule the tone to play at an exact point in time

