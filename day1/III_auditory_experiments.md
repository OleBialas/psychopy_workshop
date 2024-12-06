# Creating Reusable Experiments using Command-Line Arguments



```python
import numpy as np
from psychopy import core, sound, visual
from psychopy.hardware import keyboard
import psychtoolbox as ptb

```

## 1.


## 2. 

#### Argparse Functions: 

| Code                                            | Description |
| :---------------------------------------------- | :---------- |
| **`parser = ArgumentParser()`**                 |             |
| **`parser.print_help()`**                       |             |
| **`parser.add_argument('x', type=int)`**        |
| **`parser.add_argument('x', type=str)`**        |
| **`args = parser.parse_args(args=['a', '3'])`** |             |
| **`args.x`**                                    |             |

#### Psychopy Functions:

| Code                            | Description |
| :------------------------------ | :---------- |
| **`Sound().play()`**            |             |
| **`Sound(value=800).play()`**   |             |
| **`Sound(secs=1.5).play()`**    |             |
| **`Sound(stereo=True).play()`** |             |


**Example**


#### `args.y`

Make a parser that accepts integers for `y`:
```python
parser = ArgumentParser()
parser.add_argument('y', type=int)
parser.print_help()
```

Make `args` from the `parser` above, with `args.y` set to `10`:
```
args = parser.parse_args(args=['10'])
args.y
```

Make `args` from the `parser` above, with `args.y` set to `18`:
```
args = parser.parse_args(args=['18'])
args.y
```
---

#### `args.z`

Make a parser that accepts integers for `z`:
```python
parser = ArgumentParser()
parser.add_argument('z', type=int)
parser.print_help()
```

Make `args` from the `parser` above, with `args.z` set to `20`:
```
args = parser.parse_args(args=['20'])
args.z
```

Make `args` from the `parser` above, with `args.z` set to `55`:
```
args = parser.parse_args(args=['55'])
args.z
```

---

#### args.subject

Make a parser that accepts strings for `subject`:
```python
parser = ArgumentParser()
parser.add_argument('subject', type=str)
```

Make `args` from the `parser` above,  with `args.subject` set to `Fred`:
```python
args = parser.parse_args(args=['Fred'])
args.subject
```

---

#### args.freq
Make a parser taht accepts integers for `freq`:
```python
parser = ArgumentParser()
parser.add_argument('freq', type=int)
```

Make Psychopy play a sound at **800** Hz when `args.freq` is set to `800`.  (Hint: `Sound(value=500).play()` to play a 500 Hz)
```python
args = parser.parse_args(args=['800'])
Sound(value=args.freq).play()
```

Make Psychopy play a sound at **1200** Hz when `args.freq` is set to `1200`. 
```python
args = parser.parse_args(args=['1200'])
Sound(value=args.freq).play()
```

---

#### args.freq and args.dur


Make Psychopy play a sound for **1.8** seconds at **500** Hz when `args.freq` is set to `800` and `args.dur` is set to 1.8.  (Hint: `Sound(value=500, secs=3.2).play()` to play a 500 Hz)

Make a parser that accepts integers for `freq` and `dur`:
```python
parser = ArgumentParser()
parser.add_argument('freq', type=int)
parser.add_argument('dur', type=float)
```

Make PsychoPy play a **500** Hz tone with a duration of **1.8** seconds with `args` from the `parser` above, when `args.freq` set to `500` and `args.secs` set to `1.8`:
```python
args = parser.parse_args(args=[500, 1.8])
Sound(value=args.freq).play()
```

Make PsychoPy play a **4000** Hz tone with a duration of **0.25** seconds with `args` from the `parser` above, when `args.freq` set to `4000` and `args.secs` set to `0.25`:
```python
args = parser.parse_args(args=[4000, 0.25])
Sound(value=args.freq).play()
```
---

#### args.freq and args.stereo

Make a parser that accepts integers for `freq` and booleans for `stereo`:

```python
parser = ArgumentParser()
parser.add_argument('freq', type=int)
parser.add_argument('stereo', type=bool)
```

Make PsychoPy play a **330** Hz tone in stereo with `args` from the `parser` above, when `args.freq` set to `330` and `args.stereo` set to `True`:
```python
args = parser.parse_args(args=[330, True])
Sound(value=args.freq).play()
```

Make PsychoPy play a **2100** Hz tone in mono with `args` from the `parser` above, when `args.freq` set to `2100` and `args.stereo` set to `False`:
```python
args = parser.parse_args(args=[330, True])
Sound(value=args.freq).play()
```




## 3.  Making Your CLI Easy to Understand: Options and Help Docs

#### Argparse

| Code                                                                   | Description |
| :--------------------------------------------------------------------- | :---------- |
| **`parser = ArgumentParser(description='What this program does')`**    |             |
| **`parser.add_argument('n', help='What the n variable does')`**        |             |
| **`parser.print_help()`**                                              |             |
| **`parser.add_argument('--sub', type=str)`**                           |             |
| **`parser.add_argument('--block', type=int)`**                         |             |
| **`parser.add_argument("--do", action='store_true')`**                 |             |
| **`parser.parse_args(args=['--block', '1', '--sub', 'Bob', '--do'])`** |             |

#### Psychopy
| Code                                                   | Description |
| ------------------------------------------------------ | ----------- |
| **`keyboard.Keyboard().waitKeys()`**                   |             |
| **`keyboard.Keyboard().waitKeys(keyList=['a', 'b'])`** |             |
| **`keyboard.Keyboard().waitKeys(maxWait=3)`**          |             |
| **`keyboard.Keyboard().waitKeys(waitRelease=True)`**   |             |



## 4. Writing a program with a command line interface

- Combine sound and keypress with configuration via CLI
- Call from the terminal
- 3 exercises













## 1. Recoding responses

| Code                                       | Description                                                |
| ------------------------------------------ | ---------------------------------------------------------- |
| `clock = core.Clock()`                     | Initialize a clock to keep time                            |
| `clock.reset()`                            | Reset the timer to zero                                    |
| `keys = event.getKeys(keyList=["O", "K"])` | Return a list of all pressed keys that appear in `keyList` |
| `keys = event.waitKeys(maxWait=5)`         | Wait until a key was pressed or `maxWait` passed           |
| `keys = event.waitKeys(timeStamped=clock)` | Use an instance of `Clock` to time stamp the keypress      |



```python
# Create an instance of the Keyboard class and wait for an keypress

# Solution
kb = keyboard.Keyboard()
```

    1.27333402633667



```python
# Get all keys that have been pressed. What is the type of the returned data?

# Solution
keys = kb.getKeys()
print(type(keys))
print(type(keys[0]))
```

    <class 'list'>
    <class 'psychopy.hardware.keyboard.KeyPress'>



```python
# Clear the keyboard buffer before getting the keys

# Solution
kb.clearEvents()
kb.getKeys()
```




    []




```python
# Wait for a key press

# Solution
kb.waitKeys()
```


```python
# Wait for a press of the left or right arrow key. Print the name of the returned key.

# Solution
keys = kb.waitKeys(keyList=["left", "right"])
print(keys[0].name)
```

    left



```python
# Wait for a key press for, at maximum, 3 seconds. What is returned when 3 seconds pass without a key being pressed?

# Solution
keys = kb.waitKeys(maxWait=3)
print(keys)
```

    None



```python
# Wait for a key press and print the reaction time.

# Solution
keys = kb.waitKeys()
print(keys[0].rt)
```

    1395.6969585418701



```python
# Reset the keyboard clock, then wait for a key press and print the reaction time

# Solution
kb.clock.reset()
keys = kb.waitKeys()
print(keys[0].rt)
```

## 2. Playing Sounds

| Code                                | Description                                           |
| ----------------------------------- | ----------------------------------------------------- |
| `tone = sound.Sound("A", secs=0.5)` | Generate an A note that lasts 500 ms                  |
| `tone.play(when=now+0.5)`           | Schedule sound to play exactly 500 ms from now        |
| `tone.play(loop=3)`                 | Play the sound and repeat it in a loop                |
| `tone.stop`                         | Stop the playback of the sound                        |
| `tone.sndArray`                     | Attribute containing the sound values                 |
| `tone.setSound(x)`                  | Replace the content of `.sndArray` with the array `x` |
| `now = ptb.GetSecs()`               | Get time stamp from the PsychToolBox clock            |



```python
# Print the information about your sound device(s)

# Solution
sound.getDevices()
```


```python
# Play an 'A' note for 0.5 seconds

# Solution
tone = sound.Sound("A", secs=0.5, stereo=False)
tone.play()
```


```python
# Lower the volume of the tone to 0.2 before playing it

# Solution
tone = sound.Sound("A", secs=0.5, stereo=False)
tone.setVolume
```


```python
# Play the notes A B and C in sequence (you may use a for loop). Make sure the sounds do not overlap.

# Solution
for note in ["A", "B", "C"]:
    print(note)
    tone = sound.Sound(note, secs=0.5)
    tone.play()
    core.wait(0.5)
```


```python
# Change sound level
```


```python
# Play the Gaussian noise signal defined below

secs = 1
samplerate = 48000
signal =  np.random.randn(secs*samplerate)

# Solution
noise = sound.Sound()
noise.setSound(signal)
noise.play()
```


```python
# Generate a sound object that contains 1 second of white noise and play it in a loop 5 times.
# Play a tone 1 second after the noise started

# Solution
noise = sound.Sound()
noise.setSound(np.random.randn(48000))
tone = sound.Sound()
noise.play(loops=5)
core.wait(1)
tone.play()
```


```python
# Repeat the above exercise but schedule the tone so that it plays EXACTLY 0.5 seconds after the noise onset.

# Solution
noise = sound.Sound()
noise.setSound(np.random.randn(48000))
tone = sound.Sound()
now = ptb.GetSecs()
tone.play(when=now+0.5)
noise.play(loops=5)
core.wait(1)
tone.play()

```

## 3. Running an Auditory Experiment

### Reference table
| Code                                   | Description                                         |
| -------------------------------------- | --------------------------------------------------- |
| `parser = argparse.ArgumentParser()`   | Create a parser for command line arguments          |
| `parser.add_argument("--id" type=int)` | Add a argument called "id" of type int              |
| `args = parser.parse_args()`           | Parse the command line input                        |
| `args.id`                              | Value passed to the "id" argument                   |
| `python experiment.py --id 7`          | Run "experiment.py" and pass 7 to the "id" argument |


```python
# In same folder as this notebook, you'll find a program called audiogram.py
# Run this cell to view the documentation of that program

!python audiogram.py -h
```


```python
# Run the audiogram with a 800 Hz tone

# Solution
!python pure_tone_audiogram.py 800
```


```python
# Add a new command line argument for starting intensity
```


```python
# Add a new command line argument for subject id and indclude the ID in the printed reuslt
```


```python
# Include an optional flag for stereo sound
```


```python
# Write a new program with a CLI called "say_hi_to.py".
# This program should take in two arguments, a first and last name, and print:
# "Hi <first name> <last name>"
# Add an optional shout flag that, which included, makes the program print only upper case letters
```
