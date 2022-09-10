from predictor.individual_tests.maps.num_played import vertigo_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


vertigo_played = vertigo_played.VertigoPlayed()


def run():
    execute(vertigo_played, "vertigo_played")
