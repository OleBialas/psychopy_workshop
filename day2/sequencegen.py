import random
from typing import Literal, Tuple, List, Union, Optional, Iterable
import pandas as pd


def make_sequence(
    conditions: list, n_trials: int, min_dist: int = 0, max_iter: int = 1000
) -> list:
    n_reps = int(n_trials / len(conditions))
    trials = conditions * n_reps
    random.shuffle(trials)
    count = 0
    while has_repetitions(trials, min_dist):
        random.shuffle(trials)
        count += 1
        if count >= max_iter:
            raise StopIteration(f"Could not find a sequence after {count} iterations!")
    return trials


def has_repetitions(trials: list, min_dist: int) -> bool:
    trial_is_repeat = []
    trial_is_repeat.append(
        len(set(trials[:min_dist])) < len(trials[:min_dist])
    )  # check beginning
    for i in range(min_dist, len(trials)):  # check rest of list
        this_trial_is_repeat = []
        for j in range(1, min_dist + 1):
            # print(f"i={i}, j={j}")
            this_trial_is_repeat.append(trials[i] == trials[i - j])
        trial_is_repeat.append(any(this_trial_is_repeat))
    return any(trial_is_repeat)


def write_sequence(trials: list, fpath: str):
    data = {"trials": trials, "response": None}
    df = pd.DataFrame(data)
    df.to_csv(fpath)
