from predictor.individual_tests.maps.num_played import mirage_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


mirage_played = mirage_played.MiragePlayed()


def run(deep_analysis_doc, query):
    execute(mirage_played, "mirage_played", deep_analysis_doc, query)
