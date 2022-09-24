from predictor.individual_tests.maps.rounds_won_in_losses import nuke_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


nuke_rwil = nuke_rwil.NukeRoundsWonInLosses()


def run(deep_analysis_doc, query):
    execute(nuke_rwil, "nuke_rwil", deep_analysis_doc, query)
