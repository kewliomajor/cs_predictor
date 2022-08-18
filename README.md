## How to Use

- Have a running localhost MongoDB instance
- Run ```populate_initial_weights.py``` to create an initial entry of weights used to predict matches
- Run ```pull_incomplete_matches/pull_incomplete_matches.py``` to grab today's matches on hltv.org
- Run ```predictor/calculate_winner.py``` to pull information from each match, and run through the initial weights to calculate match winners
- After matches are completed run ```result_checker/check_results.py``` to record the actual match winner
- Run ```iteration_data_gathering/assess_results.py``` in order to run through predictions vs outcome and record a new set of weights


To assess the performance of a specific weight you can run
```iteration_data_gathering/assess_weights_performance.py```
and give it any uuid for an entry in the weights table