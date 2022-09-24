from predictor.individual_tests.maps.num_played import overpass_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


overpass_played = overpass_played.OverpassPlayed()


def run(deep_analysis_doc, query):
    execute(overpass_played, "overpass_played", deep_analysis_doc, query)
