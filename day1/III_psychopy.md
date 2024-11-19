# PsychoPy

## 0. Modules and classes

PsychoPy consists of several [modules](https://psychopy.org/py-modindex.html) that can be imported individually.
The modules we are going to use in this notebook can be imported like this:

```python
from psychopy import visual, core
from psychopy.hardware import keyboard
```
The `visual` module is for displaying visual stimuli, `core` is a collection of basic functions, like timers, and the `keyboard` module is for recording inputs.

We are going to use these models by interacting with dedicated classes.
Each of these classes represents a certain element of the experiment like a particular stimulus or the keyboard used to obtain responses.
To use these classes, one has to create an instance which is created by calling the class, as you would do with a function, for example:

```python
kb = keyboard.Keyboard()
ck = core.Clock()
```

The class instances have attributes that store data as well as methods that do things.
A method can be called like a function. For example `kb.waitKeys()`, will pause the script to wait for a key press.
The pressed keys are stored in the attribute `kb.keys`.
Note that on used round brackets to call a methods but no brackets to access an attribute.

## 1. Getting responses

In the previous notebook, we used Python's builtin `input()` function to record the participant's response.
However this function is fairly limited: it only records input that are typed to the terminal, offers no control over which responses are recorded and which aren't and it is temporally imprecise, because all inputs must be confirmed by pressing enter.

PsychoPy, on the other hand, provides methods to record specific keys and report the times they were pressed and released with high precision.
Let's create a script called `test_keys.py` that waits for a press of the space key and prints out the result:

```python
from psychopy.hardware import keyboard
kb = keyboard.Keyboard()
keys = kb.waitKeys(keyList=["space"], maxWait=5, waitRelease=True, clear=True)
print(keys)
```
The argument `maxWait` determines the maximum time to wait for a key and `waitRelease=True` means that the method will wait until the key was pressed and released again.
Setting `clear=True` means that the buffer will be cleared of all previous keys before we start waiting.

When we run this script with `python test_keys.py`, it won't do anything until you press the space key.
Once you do, it will print out the content of the variable `keys` that is returned by the `.waitKeys()` method, which should look like this:

```sh
[<psychopy.hardware.keyboard.KeyPress object at 0x000001D88A7EDED0>]
```

This tells you that the output of `.waitKeys()` is a list (note the square brackets) containing `KeyPress` objects.
The hexadecimal number `0x000001D88A7EDED0` is the address in the computer's memory where the `KeyPress` object is stores and is of no concern to us.
Just like `Keyboard`, the `KeyPress` is a class that represents an element of our experiment, namely the pressing of one key.
Each `KeyPress` has several attributes like `.name` (name of the key), `.tDown` (the time the key went down), `.duration` (how long the key was held down), and `.rt` (reaction time).
Let's change the print statement in `test_keys.py` to a message that reports these attributes:

```python
for key in keys:
    print(f"At {key.tDown}, you pressed {key.name} for {key.duration} seconds. Your reaction time was {key.rt}")
```

Now the program should print out something like this:

```sh
At 1.1220025000002352, you pressed space for 0.11906540000200039 seconds. Your reaction time was 1.1220025000002352
```

The `Keyboard` class instance contains a clock that starts running when the instance is created.
This clock is used to compute the time and duration of key presses.
You'll notice that `.tDown` and `.rt` are exactly the same.
While `.tDown` is the **absolute** time the key was pressed, `.rt` is the time **relative** to the last reset of the clock.
Since we never reset our clock, the two are identical.

Let's edit `test_keys.py` so the clock is reset right before we call `.waitKeys()`.
Instead of having the `Keyboard` class run on it's own clock, we'll create an instance of the `Clock` class and pass it to `Keyboard`.
This ensures that the keyboard runs on the same clock the experiment is using and avoids confusion.
Now our script should look like this:

```python
from psychopy import core
from psychopy.hardware import keyboard

clock = core.Clock()
kb = keyboard.Keyboard(clock=clock)

core.wait(1)  # wait for 1 second
clock.reset()
keys = kb.waitKeys(keyList=["space"], maxWait=5, waitRelease=True, clear=True)

for key in keys:
    print(
        f"At {key.tDown}, you pressed {key.name} for {key.duration} seconds. Your reaction time was {key.rt}"
    )
```

If we run this version of `test_keys.py`, we should see a different value for the time the key was pressed and the response time.
In our experiment, we can reset the clock at certain events, like the onset of a stimulus, to measure the reaction time relative to that event.

### Exercises
1. What happens if we run `test_psychopy.py` and we wait, without pressing a key, until `maxWait` has passed?
2. Modify `test_psychopy.py` so that it waits for the left or right arrow key instead of space (you can find a list of all key names [here](https://pyglet.readthedocs.io/en/latest/modules/window_key.html). What happens if you press both keys at the same time?
3. Create a `for` loop that waits for a key press multiple times in a row. What happens if you set `clear=False`?


## 2. Visual Display

For our experiment, we also have to be able to display text and images on our screen.
The screen is managed by the `Window` class from the `visual` module.
Once an instance of that class is created, a new PsychoPy window will pop up on screen.
Let's test this in a new script called `test_visual.py`:

```python
from psychopy import visual
from psychopy.hardware import keyboard

kb = keyboard.Keyboard()
win = visual.Window(size=(800,600), fullscr=False)

keys = kb.waitKeys(keyList=["space"])

win.close()
```

This will create a new 800 by 600 pixel window without making it full screen.
Then, we just wait for the space key and close our window again.
When we run this code with `python test_visual.py`, we should see a gray window pop up and then close once we press space.
In the terminal, we should find a message warning us that no monitor specification could be found.
This simply means that PsychoPy does not know certain properties of our screen like it's height and width, but that should not bother us for now.

PsychoPy uses a dual-buffering system which means that there are two virtual screens: one that is being displayed and one that is hidden.
Images are drawn to the hidden screen and only revealed one the window is flipped.
Let's modify `test_visual.py` to show a little welcome message:

```python
from psychopy import visual
from psychopy.hardware import keyboard

kb = keyboard.Keyboard()
win = visual.Window(size=(800,600), fullscr=False)

text = visual.TextStim(win, text="Welcome to the Experiment!")
text.draw()
win.flip()

keys = kb.waitKeys(keyList=["space"], maxWait=5, waitRelease=True, clear=True)

win.close()
```

The `TextStim` is another class which represents a specific text stimulus and it's first argument is the `Window` instance that the stimulus belongs to.
Once the instance is created, we can use the `.draw()` method to draw the stimulus to our screen.
However, since the stimulus is drawn to the hidden screen, we have to `.flip()` the window before we see anything.
If you run this version of `test_visual.py` you should see the welcome message appear in the center of the PsychoPy window.

One may also draw multiple images before flipping the window.
For example, we could draw a rectangle around our text:

```python
text = visual.TextStim(win, text="Welcome to the Experiment!")
text.draw()
rect = visual.Rect(win, width=1, height=1, lineColor="white")
rect.draw()
win.flip()
```

`Rect` is another class that represents a Rectangle.
PsychoPy contains many classes for [different kinds of visual stimuli](https://psychopy.org/api/visual/index.html) but they all work similar: they require a `Window` as their first argument and are drawn to the screen by calling their `.draw()` method

### Exercises
1. Change the color of the rectangle drawn around the text.
2. What happens if you call `win.flip()` twice in a row?
3. Pick to new stimuli (you can find all of them [here](https://psychopy.org/api/visual/index.html)) and draw them to the screen as well.
4. Modify `test_visual.py` so that the script displays a new image after the space key has been detected and then waits for the space key again before it terminates.

## 3. Spatial Units

You may have wondered what `width` and `height` values passed to the `Rect` class represented.
This depends on the units used by `Window`.
PsychoPy supports [several units](https://www.psychopy.org/general/units.html) like centimeters, pixels or visual angle.
The unit can be selected when creating the window instance, like this:

```python
win = visual.Window(size=(800,600), fullscr=False, units="norm")
```
Here, we use the default `norm` unit which positions elements using a normalized reference frame.
This has the advantage that PsychoPy does not need to know our screen's width, height or resolution and that the elements will always appear at the same relative locations on all screens.

The `norm` coordinate system goes from -1 to +1 where -1 represents the bottom and left and +1 represents the top and right (e.g. -1,+1 represents the left upper corner, +1,-1 represents the right lower corner).
Let's edit `test_visual.py` to position the rectangle more towards the bottom of the screen.

```python
rect = visual.Rectin, pos=(0, -0.3), width=1, height=1, lineColor="white")
```

The `pos` attribute determines the position of the rectangles center and `width` and `height` determine it's size.
You may wonder why the object you are seeing is not a square - it's width should be equal to it's height.
This is because the `norm` units are computed separately for the two dimensions. The parameters `width=1` and `height=1` make a rectangle that covers 50 % of the screens width and height, respectively.
Thus, if the screen is not square, neither will the rectangle be!
If we want to display a square, we can correct for this distortion by using `.aspect` attribute of the window class which represents how much wider than tall the screen is:

```python
rect = visual.Rect(win, pos=(0, -0.3), width=1/win.aspect, height=1, lineColor="white")
```

### Exercises
1. Change the rectangle's size so it covers the whole screen.'s size
2. Split the Welcome message into four separate messages "Welcome", "to", "the" and "Experiment" that are displayed in the top left, bottom left, top right and bottom right corners of the screen.
3. What may be downsides of using normalized units?


## 4. Timing

Exact timing is essential for experiments, especially in neuroscience where we must make sure that our devices that record brain activity are synchronized with the experimental program.
When we talk about the timing of, for example a of stimulus onset, there are two important metrics: precision and accuracy.
Accuracy refers to a constant error or "lag" that results from the physical limitations of the hardware.
For example, if the stimulus onset has an accuracy of 5 ms, the stimulus will start 5 ms after the nominal onset.
Precision refers to the variable error or "jitter" that may be caused by the operating system.
For example, if the stimulus onset has an accuracy of 5ms and a precision of 1ms, it will start between 4 and 6 ms after the nominal onset.
While we can correct for a known constant delay, we can't correct for jitter - this is why experimenters are usually more concerned about precision.

The good news is that, according to a [recent study](https://peerj.com/articles/9414/), PsychoPy is capable of delivering sub-millisecond precision.
However, this requires some careful considerations of our code and hardware.

One important factor to keep in mind is that computer screens have a fixed refresh rate, typically 60 Hz.
The `Window` class has a method for measuring the actual frame rate - let's create a script called `measure_frame_rate.py` with the following content:

```python
from psychopy import visual

win = visual.Window()
fps = win.getActualFrameRate()

print(f"The measured frame rate is {fps} Hz")
print(f"Thus, 1 frame lasts for {1/fps} s")
win.close()
```
If we run this script, we should see something like this:

```sh
The measured frame rate is 60.248767156570935 Hz
Thus, 1 frame lasts for 0.016597850000835024 s
```

The fact that the screen refreshes at fixed intervals may seem obvious, but it's consequence is that images can only be displayed for a multiple of the frame rate.
For example, displaying a stimulus for 220 ms is impossible if the screens frame rate is 60 Hz - the actual image will be displayed some fraction of a frame to long or too short.
Fortunately though, 3 frames at a 60 Hz frame rate will last exactly 50 ms, so all multiples of 50 ms are OK.

Another fact that may seem trivial is that computers need time to perform operations.
Thus, we have to account for time consuming operations in our experimental timing.
To demonstrate this, let's create a script called `test_timing.py` that contains the following:


```python
from psychopy import core, visual
from psychopy.hardware import keyboard

clock = core.Clock()
kb = keyboard.Keyboard(clock=clock)
win = visual.Window(fullscr=True)

fix_dur = 0.5  # how long the fixation is displayed
stim_dur = 0.25  # how long the stimulus is displayed

kb.waitKeys(keyList=["space"])
fix = visual.Circle(win, radius=0.1, fillColor="white")
fix.draw()
win.flip() # show fixation
t_fix = clock.getTime() # fixation onset
core.wait(fix_dur)

img = visual.ImageStim(win, image="smile.webp")  # load image
img.draw()
win.flip() # show image
t_stim = clock.getTime() # image onset
core.wait(stim_dur)

print(f"The fixation was displayed for {t_stim - t_fix}")

win.close()
```

Dropping frames


Hardware




- Effect of time consuming operations (e.g. image loading)
- Possible hardware sources for bad timing
- natural response time variability
- Screen refresh rate
- A 4k display typically has a resolution of 3840x2160 which makes roughly 8.3 million pixels. Each pixel has a red, green, blue and alpha value. At 60 frams per second, the graphics card needs to update and output a staggering 40 billion values per second. Older hardware will just decrease the refresh rate to manage the load.
- Turn off triple buffering, window scaling and any postprocessing done by the screen
- Turn off unnecessary network services (e.g. Dropbox, email) or just disconnect from the network
- Don't run any (memory intense) programs in parallel
- Keep image files to roughly the size needed on screen


## 4. Playing sounds


```python
from psychopy import prefs
prefs.hardware['audioLib'] = ['pyo']
from psychopy import sound
```

## Project

- Create a "timing checklist" for your experiment and setup.
- make an animated smiley
