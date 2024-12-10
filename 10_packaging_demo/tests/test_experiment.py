from pathlib import Path
import time
from psychopy.core import Clock # type: ignore
import experiment

WAITKEY_CALL_PER_TRIAL = 1
CIRCLE_CALL_PER_TRIAL = 3
RECT_CALL_PER_TRIAL = 6


def test_run_trial_calls(
    mock_window, mock_circle, mock_rect, mock_waitKeys, config 
):
    clock = Clock()
    experiment.run_trial(mock_window, clock, side="left", valid=True, config=config)
    assert mock_waitKeys.call_count == WAITKEY_CALL_PER_TRIAL
    assert mock_circle.call_count == CIRCLE_CALL_PER_TRIAL
    assert mock_rect.call_count == RECT_CALL_PER_TRIAL


def test_run_block_calls(
    config, mock_window, mock_circle, mock_rect, mock_waitKeys
):
    clock = Clock()
    experiment.run_block(mock_window, clock, config)
    assert mock_waitKeys.call_count == WAITKEY_CALL_PER_TRIAL * config["n_trials"]
    assert mock_circle.call_count == CIRCLE_CALL_PER_TRIAL * config["n_trials"]
    assert mock_rect.call_count == RECT_CALL_PER_TRIAL * config["n_trials"]



def test_run_experiment_calls(
    write_config, mock_window, mock_circle, mock_rect, mock_text, mock_waitKeys
):
    config = experiment.load_config(write_config)
    experiment.run_experiment(1, write_config)

    assert (
        mock_waitKeys.call_count
        == WAITKEY_CALL_PER_TRIAL * config["n_trials"] * config["n_blocks"]
        + config["n_blocks"]
        + 2
    )
    assert (
        mock_circle.call_count
        == CIRCLE_CALL_PER_TRIAL * config["n_trials"] * config["n_blocks"]
    )
    assert (
        mock_rect.call_count == RECT_CALL_PER_TRIAL * config["n_trials"] * config["n_blocks"]
    )
    assert mock_text.call_count == config["n_blocks"] + 2


def test_run_experiment_writes_files(
    write_config, mock_window, mock_circle, mock_rect, mock_text, mock_waitKeys
):
    config = experiment.load_config(write_config)
    experiment.run_experiment(1, write_config)
    files = list(Path(config["root_dir"]).glob("data/*/*"))
    assert len(files) == config["n_blocks"]


def test_trial_timing(
    config, mock_window, mock_circle, mock_rect, mock_waitKeys
):
    tic = time.time()
    clock = Clock()
    experiment.run_trial(mock_window, clock, side="left", valid=True, config=config)
    elapsed = time.time() - tic
    assert abs(elapsed - (config["fix_dur"] + config["cue_dur"])) < 0.01


def test_block_data_is_valid(
    config, mock_window, mock_circle, mock_rect, mock_waitKeys
):
    clock = Clock()
    df = experiment.run_block(mock_window, clock, config)
    assert df.shape[0] == config["n_trials"]
    assert df["side"].isin(["left", "right"]).all()
    assert df["valid"].isin([True, False]).all()
    assert df["response"].isin(["left", "right"]).all()
    assert all([isinstance(d, float) for d in df["response_time"]])
