from predictor.individual_tests.recent_history import maps_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


maps_played = maps_played.MapsPlayed()


def run(deep_analysis_doc, query):
    execute(maps_played, "maps_played", deep_analysis_doc, query)
