import os
import json
from unittest import mock
import random
import pytest
import experiment


@pytest.fixture
def config(tmp_path):
    return {
        "root_dir": str(tmp_path),
        "fix_dur": 0.01,
        "cue_dur": 0.01,
        "fix_radius": 0.1,
        "stim_radius": 0.2,
        "n_blocks": 2,
        "n_trials": 20,
        "p_valid": 0.5,
        "pos": {"left": (-0.5, 0), "right": (0.5, 0)},
        "text": {
            "hello": "Welcome to the experiment! \n \n Look at the white fixation point in the middle of the screen. \n \n When a black dot appears, indicate if it is on the left or right using the arrow keys. \n \n Respond as fast as possible! \n \n Press space to continue",
            "goodbye": "Thank you for participating! \n \n Press space to exit."
    }
    }


@pytest.fixture
def write_config(config, tmp_path):
    config["root_dir"] = str(tmp_path)
    config_fname = os.path.join(tmp_path, "sample_config.json")
    json.dump(config, open(config_fname, "w"))
    yield config_fname


@pytest.fixture
def create_temp_subject_dir(tmp_path):
    subject_dir = experiment.create_subject_dir(tmp_path, 1, False)
    return subject_dir


@pytest.fixture
def mock_window():
    with mock.patch.object(experiment, "Window") as MockWin:
        MockWin.flip.return_value = None
        MockWin.aspect = 2
        yield MockWin


@pytest.fixture
def mock_circle():
    with mock.patch.object(experiment, "Circle") as MockCircle:
        yield MockCircle


@pytest.fixture
def mock_rect():
    with mock.patch.object(experiment, "Rect") as MockRect:
        yield MockRect


@pytest.fixture
def mock_text():
    with mock.patch.object(experiment, "TextStim") as MockText:
        yield MockText


@pytest.fixture
def mock_waitKeys():
    with mock.patch("experiment.waitKeys") as mock_waitKeys:
        def mock_wait_function(keyList, timeStamped=None):
            key = random.choice(keyList)
            if timeStamped: # If timeStamped was provided, return [key, time], else just [key]
                return [(key, random.random())]
            return [key]
        
        mock_waitKeys.side_effect = mock_wait_function
        yield mock_waitKeys
