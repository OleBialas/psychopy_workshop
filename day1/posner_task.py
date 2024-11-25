import json
import pandas as pd
from psychopy import core, visual, event

#### Initialize PsychoPy classes ####
win = visual.Window(fullscr=True)
clock = core.Clock()

#### Define parameters ####
SUB_ID = "01"  # subject ID (used to create file name)
N_TRIALS = 10  # number of trials
P_VALID = 0.8  # probability that a cue is valid
FIX_DUR = 0.5  # duration for which fixation is displayed
CUE_DUR = 0.5  # duration for which cue is displayed
INSTRUCTIONS = """
    Welcome! \n
    When the experiment starts, you'll see a white dot and two white boxes. \n
    Fixate the white dot whenever it appears!
    After a short while, a red dot will appear in one box.
    Use the arrow keys to say that the red dot is in the left or right box.
    Respond as soon as possible! \n
    Before the red dot appears, one of the boxes will be highlighted red.
    Most of the time, the red dot will appear in the highlighted box.\n
    Press space to start the experiment!
    """

##### Create the trial sequence ####
side, valid = [], []
if N_TRIALS / 2 * P_VALID % 1 != 0:
    raise ValueError("Trials can't be evenly divided between conditions!")
for s in ["left", "right"]:
    n = int(N_TRIALS / 2)
    side += [s] * n
    n_valid = int(n * P_VALID)
    valid += [True] * n_valid + [False] * (n - n_valid)
trials = pd.DataFrame(
    {"stimulus_side": side, "cue_valid": valid, "response": None, "reaction_time": None}
)
trials = trials.sample(frac=1, replace=False)  # shuffle the trial order

#### Show instructions ####
text = visual.TextStim(win, text=INSTRUCTIONS, height=0.07)
text.draw()
win.flip()
event.waitKeys(keyList=["space"])
core.wait(1)

#### Run trials ####
for i_trial in trials.index:
    clock.reset()

    # show boxes and fixation
    box_left = visual.Rect(win, lineColor="white", pos=(-0.5, 0))
    box_right = visual.Rect(win, lineColor="white", pos=(0.5, 0))
    fixation = visual.Circle(win, fillColor="white", size=(0.05 / win.aspect, 0.05))
    _, _, _ = box_left.draw(), box_right.draw(), fixation.draw()
    win.flip()

    core.wait(FIX_DUR)

    # if stimulus is on the left and the cue is valid OR
    # if stimulus is on the right and the cue is invalid
    # highlight the left box
    if (
        trials.loc[i_trial].stimulus_side == "left"
        and trials.loc[i_trial].cue_valid == True
    ) or (
        trials.loc[i_trial].stimulus_side == "right"
        and trials.loc[i_trial].cue_valid == False
    ):
        box_left = visual.Rect(win, lineColor="red", pos=(-0.5, 0))
        box_right = visual.Rect(win, lineColor="white", pos=(0.5, 0))
    else:  # highlight the red box
        box_left = visual.Rect(win, lineColor="white", pos=(-0.5, 0))
        box_right = visual.Rect(win, lineColor="red", pos=(0.5, 0))
    _, _, _ = box_left.draw(), box_right.draw(), fixation.draw()
    win.flip()

    core.wait(CUE_DUR)

    # show stimulus
    box_left = visual.Rect(win, lineColor="white", pos=(-0.5, 0))
    box_right = visual.Rect(win, lineColor="white", pos=(0.5, 0))
    if trials.loc[i_trial].stimulus_side == "left":
        stim = visual.Circle(
            win, fillColor="red", pos=(-0.5, 0), size=(0.05 / win.aspect, 0.05)
        )
    else:
        stim = visual.Circle(
            win, fillColor="red", pos=(0.5, 0), size=(0.05 / win.aspect, 0.05)
        )
    _, _, _ = box_left.draw(), box_right.draw(), stim.draw()
    win.callOnFlip(clock.reset)
    win.flip()
    # get response
    keys = event.waitKeys(keyList=["left", "right"], timeStamped=clock)
    name, rt = keys[0]
    trials.loc[i_trial, "reaction_time"] = rt
    trials.loc[i_trial, "response"] = name

#### save results ####
trials.to_csv(f"posner_task_sub" + SUB_ID + ".csv", index=False)
