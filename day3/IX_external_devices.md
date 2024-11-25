# IX. External Devices

## 1. Serial port Communication

## 2. Sending Triggers to a Device

## 3. Checking Alignment


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

