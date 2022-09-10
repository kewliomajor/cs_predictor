from predictor.individual_tests.maps.rounds_lost_in_wins import inferno_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


inferno_rliw = inferno_rliw.InfernoRoundsLostInWins()


def run():
    execute(inferno_rliw, "inferno_rliw")
