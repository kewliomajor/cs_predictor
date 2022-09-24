from predictor.individual_tests.maps.win_percentage import ancient_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


ancient_won = ancient_won.AncientWon()


def run(deep_analysis_doc, query):
    execute(ancient_won, "ancient_won", deep_analysis_doc, query)
