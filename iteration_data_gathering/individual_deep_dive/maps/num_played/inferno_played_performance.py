from predictor.individual_tests.maps.num_played import inferno_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


inferno_played = inferno_played.InfernoPlayed()


def run(deep_analysis_doc, query):
    execute(inferno_played, "inferno_played", deep_analysis_doc, query)
