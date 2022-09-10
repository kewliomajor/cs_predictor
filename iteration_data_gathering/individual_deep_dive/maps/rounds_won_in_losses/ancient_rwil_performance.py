from predictor.individual_tests.maps.rounds_won_in_losses import ancient_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


ancient_rwil = ancient_rwil.AncientRoundsWonInLosses()


def run():
    execute(ancient_rwil, "ancient_rwil")
