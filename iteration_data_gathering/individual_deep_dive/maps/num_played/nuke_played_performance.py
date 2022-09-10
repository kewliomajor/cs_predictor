from predictor.individual_tests.maps.num_played import nuke_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


nuke_played = nuke_played.NukePlayed()


def run():
    execute(nuke_played, "nuke_played")
