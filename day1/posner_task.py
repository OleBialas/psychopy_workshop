import json
import pandas as pd
from psychopy import core, visual
from psychopy.hardware import keyboard

# Initialize PsychoPy classes
win = visual.Window(fullscr=False)
clock = core.Clock()
kb = keyboard.Keyboard(clock=clock)

with open("posner_task_cfg.json") as f:
    cfg = json.load(f)

sub_id = "01"  # subject ID


# Create the trial sequence
side, valid = [], []
if cfg["n_trials"] / 2 * cfg["p_valid"] % 1 != 0:
    raise ValueError("Trials can't be evenly divided between conditions!")
for s in ["left", "right"]:
    n = int(cfg["n_trials"] / 2)
    side += [s] * n
    n_valid = int(n * cfg["p_valid"])
    valid += [True] * n_valid + [False] * (n - n_valid)
trials = pd.DataFrame(
    {"stimulus_side": side, "cue_valid": valid, "response": None, "reaction_time": None}
)
trials = trials.sample(frac=1, replace=False)  # shuffle the trial order

# Run trials
for i_trial in trials.index:
    clock.reset()

    # show boxes and fixation
    box_left = visual.Rect(win, lineColor="white", pos=(-0.5, 0))
    box_right = visual.Rect(win, lineColor="white", pos=(0.5, 0))
    fixation = visual.Circle(fillColor="white", size=(0.05 / win.aspect, 0.05))
    _, _, _ = box_left.draw(), box_right.draw(), fixation.draw()
    win.flip()

    core.wait(clock.getTime() - cfg["fixdur"])

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

    core.wait((cfg["cue_dur"] + cfg["fix_dur"]) - clock.getTime())

    # show stimulus
    box_left = visual.Rect(win, lineColor="white", pos=(-0.5, 0))
    box_right = visual.Rect(win, lineColor="white", pos=(0.5, 0))
    if trials.loc[i_trial].stimulus_side == "left":
        stim = visual.Circle(
            win, fillColor="read", pos=(-0.5, 0), size=(0.05 / win.aspect, 0.05)
        )
    else:
        stim = visual.Circle(
            win, fillColor="red", pos=(0.5, 0), size=(0.05 / win.aspect, 0.05)
        )
    _, _, _ = box_left.draw(), box_right.draw(), stim.draw()
    t_stimulus_onset = win.getFutureFlipTime(clock=clock)
    win.flip()

    # get response
    key = kb.waitKeys(keyList=["left", "right"])
    trials.loc[i_trial].reaction_time = key.rt - t_stimulus_onset
    trials.loc[i_trial].reaction_time = key.name

# save results
trials.to_csv(f"posner_task_sub{sub_id}.csv")
