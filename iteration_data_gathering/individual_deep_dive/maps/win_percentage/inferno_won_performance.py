from predictor.individual_tests.maps.win_percentage import inferno_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


inferno_won = inferno_won.InfernoWon()


def run():
    execute(inferno_won, "inferno_won")
