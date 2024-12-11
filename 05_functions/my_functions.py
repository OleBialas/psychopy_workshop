from typing import Dict

def get_stimulus_properties(stim_id: str) -> Dict:
    """Get stimulus duration and position."""
    return {
        "duration": 0.5,
        "position_x": 0.0,
        "position_y": 0.0
    }

def present_stimulus(stim_id: str) -> None:
    props = get_stimulus_properties(stim_id)
    duration = props["duraton"]  # Typo in key!