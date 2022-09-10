from predictor.individual_tests.maps.rounds_won_in_losses import vertigo_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


vertigo_rwil = vertigo_rwil.VertigoRoundsWonInLosses()


def run():
    execute(vertigo_rwil, "vertigo_rwil")
