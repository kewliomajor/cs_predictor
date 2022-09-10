from predictor.individual_tests.maps.rounds_won_in_losses import inferno_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


inferno_rwil = inferno_rwil.InfernoRoundsWonInLosses()


def run():
    execute(inferno_rwil, "inferno_rwil")
