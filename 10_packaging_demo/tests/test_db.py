import pytest
from experiment import create_subject_dir

def test_subject_dir_is_only_overwritten_when_requested(create_temp_subject_dir):
    assert create_subject_dir(create_temp_subject_dir, 1, True)
    with pytest.raises(FileExistsError):
        create_subject_dir(create_temp_subject_dir, 1, False)