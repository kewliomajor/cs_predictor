import pymongo
from predictor.individual_tests import head_to_head, rank_difference
from predictor.individual_tests.maps import ancient, dust2, inferno, mirage, nuke, overpass, vertigo
from predictor.individual_tests.recent_history import maps_lost, maps_won, match_win_percentage, matches_won, matches_lost
from model import mongo_client


def get_score(test, entity_name):
    test_winner = test.calculate_winner(match)
    test_score = test.get_base_score(match)
    test_weight = test.get_weight(current_weights)

    if test_weight is None:
        return 0

    if test_winner == entity_name:
        return test_score * test_weight
    else:
        return 0


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

not_predicted = matches_doc.find({"prediction": None})

head_to_head = head_to_head.HeadToHead()
rank_difference = rank_difference.RankDifference()

ancient = ancient.Ancient()
dust2 = dust2.Dust2()
inferno = inferno.Inferno()
mirage = mirage.Mirage()
nuke = nuke.Nuke()
overpass = overpass.Overpass()
vertigo = vertigo.Vertigo()

maps_lost = maps_lost.MapsLost()
maps_won = maps_won.MapsWon()
match_win_percentage = match_win_percentage.MatchesWinPercentage()
matches_won = matches_won.MatchesWon()
matches_lost = matches_lost.MatchesLost()

for match in not_predicted:
    team_score = 0
    opponent_score = 0
    team_name = match["team"]["name"]
    opponent_name = match["opponent"]["name"]

    # head to head
    team_score += get_score(head_to_head, team_name)
    opponent_score += get_score(head_to_head, opponent_name)

    # rank difference
    team_score += get_score(rank_difference, team_name)
    opponent_score += get_score(rank_difference, opponent_name)

    # maps
    team_score += get_score(ancient, team_name)
    opponent_score += get_score(ancient, opponent_name)
    team_score += get_score(dust2, team_name)
    opponent_score += get_score(dust2, opponent_name)
    team_score += get_score(inferno, team_name)
    opponent_score += get_score(inferno, opponent_name)
    team_score += get_score(mirage, team_name)
    opponent_score += get_score(mirage, opponent_name)
    team_score += get_score(nuke, team_name)
    opponent_score += get_score(nuke, opponent_name)
    team_score += get_score(overpass, team_name)
    opponent_score += get_score(overpass, opponent_name)
    team_score += get_score(vertigo, team_name)
    opponent_score += get_score(vertigo, opponent_name)

    # history
    team_score += get_score(maps_lost, team_name)
    opponent_score += get_score(maps_lost, opponent_name)
    team_score += get_score(maps_won, team_name)
    opponent_score += get_score(maps_won, opponent_name)
    team_score += get_score(match_win_percentage, team_name)
    opponent_score += get_score(match_win_percentage, opponent_name)
    team_score += get_score(matches_won, team_name)
    opponent_score += get_score(matches_won, opponent_name)
    team_score += get_score(matches_lost, team_name)
    opponent_score += get_score(matches_lost, opponent_name)

    if team_score >= opponent_score:
        winner = team_name
    else:
        winner = opponent_name

    matches_doc.update_one({"_id": match["_id"]}, {"$set": {"prediction": winner, "weights_id": current_weights["_id"]}})
