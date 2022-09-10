from predictor.individual_tests.maps.num_played import ancient_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


ancient_played = ancient_played.AncientPlayed()


def run():
    execute(ancient_played, "ancient_played")
