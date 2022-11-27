from predictor.individual_tests.maps.rounds_won_in_losses import anubis_rwil
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


anubis_rwil = anubis_rwil.AnubisRoundsWonInLosses()


def run(deep_analysis_doc, query):
    execute(anubis_rwil, "anubis_rwil", deep_analysis_doc, query)
