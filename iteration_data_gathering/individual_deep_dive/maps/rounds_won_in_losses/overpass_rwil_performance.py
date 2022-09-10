from predictor.individual_tests.maps.rounds_won_in_losses import overpass_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


overpass_rwil = overpass_rwil.OverpassRoundsWonInLosses()


def run():
    execute(overpass_rwil, "overpass_rwil")
