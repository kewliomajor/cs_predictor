from predictor.individual_tests import rank_difference
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


rank_difference = rank_difference.RankDifference()


def run(deep_analysis_doc, query):
    execute(rank_difference, "rank_difference", deep_analysis_doc, query)
