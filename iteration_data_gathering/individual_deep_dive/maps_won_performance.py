from predictor.individual_tests.recent_history import maps_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


maps_won = maps_won.MapsWon()


def run():
    execute(maps_won, "maps_won")
