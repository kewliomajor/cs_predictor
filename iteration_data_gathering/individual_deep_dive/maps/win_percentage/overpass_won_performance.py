from predictor.individual_tests.maps.win_percentage import overpass_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


overpass_won = overpass_won.OverpassWon()


def run():
    execute(overpass_won, "overpass_won")
