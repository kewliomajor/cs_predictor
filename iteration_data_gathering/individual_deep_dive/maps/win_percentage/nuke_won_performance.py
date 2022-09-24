from predictor.individual_tests.maps.win_percentage import nuke_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


nuke_won = nuke_won.NukeWon()


def run(deep_analysis_doc, query):
    execute(nuke_won, "nuke_won", deep_analysis_doc, query)
