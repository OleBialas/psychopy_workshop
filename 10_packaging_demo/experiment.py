import argparse
import json
import random
import shutil
from pathlib import Path
from unittest.mock import patch
import pandas as pd
from psychopy.event import waitKeys # type: ignore
from psychopy.visual import Window, Rect, Circle, TextStim # type: ignore
from psychopy.core import Clock, wait # type: ignore


def run_experiment(subject_id: int, config_file: str, overwrite: bool = False):

    config = load_config(config_file)
    subject_dir = create_subject_dir(config["root_dir"], subject_id, overwrite)
    with Window() as win:
        clock = Clock()
        draw_text(win, "hello", config=config, flip=True)
        waitKeys(keyList=["space"])

        for i in range(config["n_blocks"]):
            draw_text(
                win, f"block {i+1} of {config['n_blocks']}", config=config, flip=True
            )
            waitKeys(keyList=["space"])

            trials = run_block(win, clock, config)
            trials.to_csv(subject_dir / f"block_{i+1}.csv", index=False)

        draw_text(win, "goodbye", config=config, flip=True)
        waitKeys(keyList=["space"])


def run_block(win: Window, clock: Clock, config: dict) -> pd.DataFrame:
    trials = make_sequence(config["n_trials"], config["p_valid"])
    for i in trials.index:
        key = run_trial(win, clock, trials.loc[i].side, trials.loc[i].valid, config)
        trials.loc[i, "response"] = key[0]
        trials.loc[i, "response_time"] = key[1]
    return trials


def run_trial(win: Window, clock: Clock, side: str, valid: bool, config: dict) -> list:

    draw_frames(win, config)
    draw_fixation(win, config, flip=True)

    wait(config["fix_dur"])

    draw_fixation(win, config)
    if (side == "left" and valid) or (side == "right" and not valid):
        draw_frames(win, config, highlight="left", flip=True)
    else:
        draw_frames(win, config, highlight="right", flip=True)

    wait(config["cue_dur"])

    draw_frames(win, config)
    draw_stimulus(win, config, side, flip=True)
    clock.reset()

    keys = waitKeys(keyList=["left", "right"], timeStamped=clock)
    return keys[0]


def make_sequence(n_trials: int, p_valid: float) -> pd.DataFrame:
    side, valid = [], []
    if n_trials / 2 * p_valid % 1 != 0:
        raise ValueError("Trials can't be evenly divided between conditions!")
    for s in ["left", "right"]:
        n = int(n_trials / 2)
        side += [s] * n
        n_valid = int(n * p_valid)
        valid += [True] * n_valid + [False] * (n - n_valid)
    trials = pd.DataFrame(
        {"side": side, "valid": valid, "response": None, "response_time": None}
    )
    return trials.sample(frac=1).reset_index(drop=True)


def draw_frames(win: Window, config: dict, highlight: str = "", flip: bool = False):
    for side in ["left", "right"]:
        if side == highlight:
            color = "red"
        else:
            color = "white"
        frame = Rect(win, lineColor=color, pos=config["pos"][side])
        frame.draw()
    if flip:
        win.flip()


def draw_fixation(win: Window, config: dict, flip: bool = False):
    fixation = Circle(
        win, radius=config["fix_radius"], size=(1 / win.aspect, 1), fillColor="white"
    )
    fixation.draw()
    if flip:
        win.flip()


def draw_stimulus(win: Window, config: dict, side: str, flip: bool = False):
    stimulus = Circle(
        win,
        pos=config["pos"][side],
        radius=config["stim_radius"],
        size=(1 / win.aspect, 1),
        fillColor="red",
        lineColor=None,
    )
    stimulus.draw()
    if flip:
        win.flip()


def draw_text(win: Window, message: str, config: dict, flip: bool = False):
    if message == "hello" or message == "goodbye":
        text = config["text"][message]
    else:
        text = f"Press space to start {message}"
    text_stim = TextStim(win, text=text)
    text_stim.draw()
    if flip:
        win.flip()


def create_subject_dir(root: Path, subject_id: int, overwrite: bool) -> Path:
    subject = f"sub-{str(subject_id).zfill(2)}"
    subject_dir = Path(root) / "data" / subject
    if subject_dir.exists():
        if overwrite is True:
            pass
        else:
            raise FileExistsError(
                f"Folder for subject {subject} already exists! \n Change the subject ID or use the --overwrite flag!"
            )
    else:
        subject_dir.mkdir(parents=True)
    return subject_dir


def load_config(config_file: str) -> dict:
    if not Path(config_file).exists():
        raise FileNotFoundError(f"Couldn't find config file at {config_file}")
    config = json.load(open(config_file))
    return config

def test_experiment(subject_id: int, config: str, overwrite: bool = False):
    def mock_waitKeys(keyList, timeStamped=None):
        print("Mock is being called!")  # Debug print
        key = random.choice(keyList)
        if timeStamped:
            return [(key, random.random())]
        return [key]

    with patch('psychopy.event.waitKeys', new=mock_waitKeys):
        import experiment
        experiment.run_experiment(subject_id, config, overwrite)

    # clean up
    root = json.load(open(config))["root_dir"]
    sub_dir = Path(root) / "data" / f"sub-{str(subject_id).zfill(2)}"
    shutil.rmtree(sub_dir)

def main_cli():
    parser = argparse.ArgumentParser(
        description="A PsychoPy implementation of the Posner attention cueing task"
    )
    parser.add_argument(
        "subject_id", type=int, help="ID of the current subject (e.g. 3)"
    )
    parser.add_argument(
        "config", type=str, help="Path to the config file (e.g. /path/to/config.json)"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing data for this subject",
    )
    parser.add_argument("--test", action="store_true", help="Run an automated test")
    args = parser.parse_args()
    if args.test is False:
        run_experiment(args.subject_id, args.config, args.overwrite)
    else:
        test_experiment(args.subject_id, args.config, args.overwrite)


if __name__ == "__main__":
    main_cli()
