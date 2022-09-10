from predictor.individual_tests.maps.win_percentage import mirage_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


mirage_won = mirage_won.MirageWon()


def run():
    execute(mirage_won, "mirage_won")
