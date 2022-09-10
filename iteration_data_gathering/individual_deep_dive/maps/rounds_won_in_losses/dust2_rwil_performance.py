from predictor.individual_tests.maps.rounds_won_in_losses import dust2_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


dust2_rwil = dust2_rwil.Dust2RoundsWonInLosses()


def run():
    execute(dust2_rwil, "dust2_rwil")
