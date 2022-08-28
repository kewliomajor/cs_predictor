from predictor.individual_tests.recent_history import maps_lost
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


maps_lost = maps_lost.MapsLost()


def run():
    execute(maps_lost, "maps_lost")
