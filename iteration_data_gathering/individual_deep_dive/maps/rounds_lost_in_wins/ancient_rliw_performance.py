from predictor.individual_tests.maps.rounds_lost_in_wins import ancient_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


ancient_rliw = ancient_rliw.AncientRoundsLostInWins()


def run():
    execute(ancient_rliw, "ancient_rliw")
