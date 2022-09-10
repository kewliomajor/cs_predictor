from predictor.individual_tests.maps.rounds_won_in_losses import nuke_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


nuke_rwil = nuke_rwil.NukeRoundsWonInLosses()


def run():
    execute(nuke_rwil, "nuke_rwil")
