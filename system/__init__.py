from .system import System
from .detectors import build_detector
from .trackers import build_tracker

def build_system(config):
    """
    Build and return a system based on the provided configuration.
    """
    # Build detector and tracker using the config
    detector = build_detector(config.detector)
    tracker = build_tracker(config.tracker)

    # Create and return a System object with detector and tracker
    return System(detector=detector, tracker=tracker)