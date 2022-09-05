from predictor.individual_tests.players import lowest_player
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


lowest_player = lowest_player.LowestPlayer()


def run():
    execute(lowest_player, "lowest_player")
