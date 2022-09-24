from predictor.individual_tests.maps.rounds_lost_in_wins import nuke_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


nuke_rliw = nuke_rliw.NukeRoundsLostInWins()


def run(deep_analysis_doc, query):
    execute(nuke_rliw, "nuke_rliw", deep_analysis_doc, query)
