
# 1. with 

### Example + 2 Exercises
```python
f = open('file.txt', 'w')
f.write('text')
f.close()
```

### Example + 3-4 Exercises
```python
with open('file.txt', 'w') as f:
    f.write('text')
```

```python
with open('file.txt', 'r') as f:
    text = f.read()
```



# 2. with Dicts and JSON

### Example + 4-5 Exercises
```python
data = {'a': 3, 'b': 'Hi'}
with open('file.txt', 'w') as f:
    json.dump(f, indent=3)
```

```python
with open('file.txt', 'r') as f:
    data = json.load(f)
data['a']
```

# 3. with Psychopy Window
```python
data = {'a': 3, 'b': 'Hi'}
with open('file.txt', 'w') as f:
    json.dump(f, indent=3)
```

```python
with open('file.txt', 'r') as f:
    data = json.load(f)

with visual.Window() as win:
    Text().draw()
    # Rect(pos=data['x'], size=data['size'], color=data['color']).draw()
    win.flip()
    Keyboard().waitKeys(keyList=['space'])
```

# 4.  Above, but In a Script

-- bonus exercise: use ArgumentParser to supply a config file










# Configuring Experiments

## 1. 

## 2. Dictionaries
do this one last

## 3. Reading and writing config files

## 4. Configuring a visual experiment

## 5. Combining Config file and CLI


# IV. Configuring an Experiment


```python
from psychopy import core, visual
from psychopy.hardware import keyboard
```

## 1. Showing Visual Stimuli

| Code                                                            | Description                                             |
| --------------------------------------------------------------- | ------------------------------------------------------- |
| `win = visual.Window(size=(800,600))`                           | Create an Window that is 800x600 pixels                 |
| `win.flip()`                                                    | Clear the screen and display new image                  |
| `win.close()`                                                   | Close the Window (usually at the end of the experiment) |
| `text = visual.textstim(win, text="hi!")`                       | Create a text object for the given `Window`             |
| `rect = visual.Rect(win, width=1, height=1, lineColor="white")` | Create a rectangle for the given `Window`               |
| `rect.draw()`                                                   | Draw a visual stimulus (e.g. rectangle) to the buffer   |


```python
# Open a Window, wait for a keypress and close it again

# Solution
kb = keyboard.Keyboard()
win = visual.Window()
kb.waitKeys()
win.close()

```




    [<KeyPress: t=23.77180552482605, value=space, duration=0.1046750545501709>]




```python
# Make the window fullscreen

# Solution
win = visual.Window(fullscr=True)
kb.waitKeys()
win.close()
```


```python
# Draw a text to the window that says:
# Welcome to the experiment!
# (Press space to continue)
# Then wait for the space key and close the window

text = "Welcome to the experiment! \n (Press space to continue)"

# Solution
kb = keyboard.Keyboard()
win = visual.Window()
text_stim = visual.TextStim(win, text=text)
text_stim.draw()
win.flip()
kb.waitKeys()
win.close()
```


```python
# Increase the fontsize of the text

# Solution
win = visual.Window()
text = "Welcome to the experiment! \n (Press space to continue)"
text_stim = visual.TextStim(win, text=text, height=0.2)
text_stim.draw()
win.flip()
kb.waitKeys(keyList=['space'])
win.close()
```

    37149.9298 	WARNING 	Monitor specification not found. Creating a temporary one...



```python
# Draw a rectangle with height and width equal to 1 and wait for a key press. 
# How does the resulting shape look?  What does that tell you about the coordinate system?

# Solution
win = visual.Window()
rect = visual.Rect(win, width=1, height=1, lineColor='white')
rect.draw()
win.flip()
kb.waitKeys()
win.close()

```


```python
# Use two flips
```


```python
# Draw the image `smile.png` in the `day1` folder to a fullscreen window, wait for 2 seconds and close the window again

# Solution
win = visual.Window(fullscr=True)
image = visual.ImageStim(win, image="smile.png")
image.draw()
win.flip()
core.wait(2)
win.close()
```

    37908.0412 	WARNING 	Monitor specification not found. Creating a temporary one...
    37908.1641 	WARNING 	User requested fullscreen with size [800 600], but screen is actually [1920, 1080]. Using actual size



```python
# Draw a rectangle around the smiley face.

# Solution
win = visual.Window()
image = visual.ImageStim(win, image="smile.png")
rect = visual.Rect(win, height=1.8, width=1.5, lineColor="white")
image.draw()
rect.draw()
win.flip()
core.wait(2)# Draw a circle with radius 0.1 to every corner of the screen (you may use a for loop to do this)

# Solution
win = visual.Window()
positions = [(-0.8, 0.8), (0.8, -0.8), (0.8, 0.8), (-0.8, -0.8)]
for pos in positions:
    circle = visual.Circle(win, radius=0.1, pos=pos, lineColor="white")
    circle.draw()
win.flip()
kb.waitKeys()
win.close()
win.close()
```

    39077.0154 	WARNING 	Monitor specification not found. Creating a temporary one...



```python
%%capture
!python posner_task.py

```

## 2. Dicts

## 2.Experimental Configuration

### Reference Table
| Code                           | Description                                                            |
| ------------------------------ | ---------------------------------------------------------------------- |
| `f = open("config.json", "w")` | Open a file called `"config.json"` in `"w"` (writing) mode             |
| `f = open("config.json", "r")` | Open a file called `"config.json"` in `"r"` (reading) mode             |
| `f.close()`                    | Close the file `f`                                                     |
| `x = {"dur": 0.5, "freq":500}` | Define a dictionary and assign it to the variable `x`                  |
| `json.dump(x, f)`              | Save the dictionary `x` to the (opened) file `f`                       |
| `json.load(f)`                 | Load a dictionary from the (opened) JSON file `f` and assign it to `x` |


```python
import json
```


```python
# add stuff about dict
```


```python
# Write the dictionary `cfg` to a .json file
cfg = {"conditions": ["a", "b", "c"], "probability": [0.2, 0.2, 0.6]}

# Solution
f = open("test_config.json", "w")
json.dump(cfg, f)
f.close()
```


```python
# Load the configuration file `tone_detection_config.json` and print out it's contents
config_fname = "tone_detection_config.json"

# Solution
f = open(config_fname, "r")
cfg = json.load(f)
f.close()
print(cfg)
```

    {'freqs': [800, 1000, 1200], 'dB_start': 65, 'dB_step:': 1.5, 'n_reversals': 5}



```python
# Open `tone_detection_config.json` in your editor, increase the number of reversals, decrease the step size and save the file. 
# Then load the config and print out the value of `n_trials` to confirm it was modified

# Solution
f = open(config_fname, "r")
cfg = json.load(f)
f.close()
print(cfg)
```

    {'freqs': [800, 1000, 1200], 'dB_start': 65, 'dB_step:': 1.5, 'n_reversals': 5}



```python
# Load the config file `posner_task_config.json` and print out it's contents
config_fname = "posner_task_config.json"

# Solution
f = open(config_fname, "r")
cfg = json.load(f)
f.close()
print(cfg)
```

    {'n_trials': 10, 'p_valid': 0.8, 'fix_dur': 0.5, 'cue_dur': 0.5}



```python
# Modify posner_task.py so that it loads `posner_task_config.json` and
# replace the paramteres defined at the beginning of the script with those from the file.
# Then, run `posner_task.py`
```


```python
# Change the value of `fix_dur` to 1 and the value of `cue` dur to 0.5.
# Rerun `posner_task.py` to see the effect of the changes.
```


```python
# Include the coordinates for the left and right side that are passed to the `pos` argument of the
# `Rect` and `Circle` class in `posner_task_config.json`. Replace all occurrences with the
# respective values from the config. Run the experiment to confirm your modification worked.
```

## 3. Config + CLI


```python
# Get the frame rate
```


```python
# get future flip time
```


```python
# calculate the time it takes to load and draw an image
```
