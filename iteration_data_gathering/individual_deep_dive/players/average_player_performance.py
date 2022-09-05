from predictor.individual_tests.players import average_player
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


average_player = average_player.AveragePlayer()


def run():
    execute(average_player, "average_player")
