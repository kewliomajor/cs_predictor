from predictor.individual_tests import rank
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


rank = rank.Rank()


def run(deep_analysis_doc, query):
    execute(rank, "rank", deep_analysis_doc, query)
