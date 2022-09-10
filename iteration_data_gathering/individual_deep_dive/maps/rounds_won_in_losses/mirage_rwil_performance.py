from predictor.individual_tests.maps.rounds_won_in_losses import mirage_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


mirage_rwil = mirage_rwil.MirageRoundsWonInLosses()


def run():
    execute(mirage_rwil, "mirage_rwil")
