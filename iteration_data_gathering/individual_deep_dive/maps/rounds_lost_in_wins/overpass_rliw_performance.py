from predictor.individual_tests.maps.rounds_lost_in_wins import overpass_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


overpass_rliw = overpass_rliw.OverpassRoundsLostInWins()


def run():
    execute(overpass_rliw, "overpass_rliw")
