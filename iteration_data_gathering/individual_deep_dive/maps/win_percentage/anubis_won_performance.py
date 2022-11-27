from predictor.individual_tests.maps.win_percentage import anubis_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


anubis_won = anubis_won.AnubisWon()


def run(deep_analysis_doc, query):
    execute(anubis_won, "anubis_won", deep_analysis_doc, query)
