from sequencegen import has_repetitions, make_sequence, save_sequence, load_sequence
import pytest

def test_has_repetitions():
    assert has_repetitions([1,2]) == False
    assert has_repetitions([1,1]) == True

def test_has_repetitions_respects_min_dist():
    assert has_repetitions([1,2,3,1], 2) == False
    assert has_repetitions([1,2,3,1], 3) == True

@pytest.mark.parametrize("n_trials", range(1, 1000))
def test_sequence_has_correct_len(n_trials):
    assert len(make_sequence([1], n_trials)) == n_trials

@pytest.mark.parametrize("conditions,max_iter", [
    ([1,2], 2),
    ([1,2,3], 3),
    ([1,2,3,4], 4)
])
def test_max_iteration(conditions, max_iter):
    with pytest.raises(StopIteration):
        make_sequence(conditions, 10, max_iter)

def test_save_and_load_sequence():
    trials = [1,2,3,4]
    fname = 'test_trials.txt'
    save_sequence(trials, fname)
    loaded = load_sequence(fname)
    assert trials == loaded