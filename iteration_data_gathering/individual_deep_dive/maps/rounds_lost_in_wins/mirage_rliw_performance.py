from predictor.individual_tests.maps.rounds_lost_in_wins import mirage_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


mirage_rliw = mirage_rliw.MirageRoundsLostInWins()


def run(deep_analysis_doc, query):
    execute(mirage_rliw, "mirage_rliw", deep_analysis_doc, query)
