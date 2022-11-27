## How to Use

- Have a running localhost MongoDB instance
- Run ```populate_initial_weights.py``` to create an initial entry of weights used to predict matches
- Run ```pull_incomplete_matches/pull_predict_check_results.py``` to record winners, grab today's matches on hltv.org, then predict new match winners


To assess the performance of a specific weight, and to get the correlation between winning individual tests and winning the entire match run
```update_all.py```
and make sure to give it any uuid for an entry in the weights table in file
```iteration_data_gathering/assess_weights_performance/assess_weights_base.py```

To simulate scenarios in the current data set run
```iteration_data_gathering/best_weight_trials/trial_find_best_weights.py```
by default it runs 1000 simulations per script run and updates the ```metadata/trial_weights_v2``` table to give you the weights to maximize the correct prediction percentage.
If you want to make the current set of weights equal to the calculated best predictors, you need to manually update the table
```metadata/current_weights_v2``` with the results from the trials

This will also populate some data for deeper analysis, which can be plotted using
any script in ```data_visualizer``` will give you a scatter plot with a regression line