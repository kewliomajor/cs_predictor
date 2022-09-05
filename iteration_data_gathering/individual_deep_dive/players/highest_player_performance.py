from predictor.individual_tests.players import highest_player
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


highest_player = highest_player.HighestPlayer()


def run():
    execute(highest_player, "highest_player")
