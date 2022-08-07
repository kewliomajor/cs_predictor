## How to Use

- Have a running localhost MongoDB instance
- Run ```predictor/populate_initial_weights.py``` to create an initial entry of weights used to predict matches
- Run ```pull_incomplete_matches/pull_incomplete_matches.py``` to grab today's matches on hltv.org
- Run ```predictor/calculate_winner.py``` to pull information from each match, and run through the initial weights to calculate match winners
- After matches are completed run ```result_checker/check_results.py``` to record the actual match winner
- Run ```predictor/assess_results.py``` in order to run through predictions vs outcome and record a new set of weights