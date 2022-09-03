from model import map_class, match_class, match_history_class, team_class
import re
import requests
from bs4 import BeautifulSoup

RANK_INDEX = 1
MAP_PERCENTAGE_INDEX = 0
base_url = "https://www.hltv.org"


def process_match(match_page):
    rankings = match_page.find_all("div", class_="lineup standard-box")
    map_wins = match_page.find("div", class_="map-stats-infobox")
    match_history = match_page.find("div", class_="past-matches")
    head_to_head = match_page.find("div", class_="head-to-head")
    analytics = match_page.find("div", class_="matchpage-analytics-section")

    match_object = match_class.Match(team_class.Team(), team_class.Team(), 0, 0, 0)

    process_rankings(rankings, match_object)
    if map_wins is not None:
        process_map_wins(map_wins, match_object)
    if match_history is not None:
        process_match_history(match_history, match_object)
    if head_to_head is not None:
        process_head_to_head(head_to_head, match_object)
    if analytics is not None:
        process_analytics(analytics, match_object)

    return match_object


def process_rankings(rankings, match_object):
    if len(rankings) > 0:
        team_num = 0
        for ranking in rankings:
            team_name = ranking.find("a", class_="text-ellipsis")
            ranking = ranking.find("a", class_="a-reset")
            if team_num == 0:
                match_object.team.name = team_name.string
            elif team_num == 1:
                match_object.opponent.name = team_name.string
            else:
                return
            if ranking is not None:
                rank_string = ranking.contents[RANK_INDEX]
                rank_string = rank_string.replace("#", "")
                if team_num == 0:
                    match_object.team.ranking = int(rank_string)
                elif team_num == 1:
                    match_object.opponent.ranking = int(rank_string)
                else:
                    return
            else:
                if team_num == 0:
                    match_object.team.ranking = 999
                elif team_num == 1:
                    match_object.opponent.ranking = 999
                else:
                    return
            team_num += 1


def process_map_wins(map_wins, match_object):
    maps = map_wins.find_all("div", class_="map-stats-infobox-maps")
    maps_regex = re.compile('(^[0-9]+) .*')

    for cs_map in maps:
        name = cs_map.find("div", class_="mapname").string
        team_stats = cs_map.find_all("div", class_="map-stats-infobox-stats")
        team_num = 0
        for stats in team_stats:
            maps_played = stats.find("div", class_="map-stats-infobox-maps-played").string
            win_percentage = stats.find("a", class_="a-reset").contents[MAP_PERCENTAGE_INDEX]
            maps_match = maps_regex.match(maps_played)

            if win_percentage == "-":
                win_percentage = 0
            else:
                win_percentage = win_percentage.replace("%", "")

            map_object = map_class.CsMap(name, int(maps_match.group(1)), int(win_percentage))
            if team_num == 0:
                match_object.team.maps.append(map_object)
            elif team_num == 1:
                match_object.opponent.maps.append(map_object)
            else:
                return

            team_num += 1


def process_match_history(match_history, match_object):
    tables = match_history.find_all("table", class_="past-matches-table")
    score_regex = re.compile('(^[0-9]+) - ([0-9]+)$')

    team_num = 0
    for table in tables:
        if team_num < 2:
            team_num += 1
            continue

        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        for row in rows:
            opponent = row.find("a", class_="text-ellipsis")
            if opponent is None:
                continue
            opponent = opponent.string
            num_maps_col = row.find("td", class_="past-matches-map")
            num_maps = num_maps_col.find("a").string

            if "bo" in num_maps:
                num_maps = int(num_maps.replace("bo", ""))
            else:
                num_maps = 1

            score_col = row.find("td", class_="past-matches-score")
            score = score_col.find("a", class_="past-matches-cell").string
            score_match = score_regex.match(score)

            match_history_object = match_history_class.MatchHistory(opponent, int(num_maps), int(score_match.group(1)), int(score_match.group(2)))
            if team_num == 2:
                match_object.team.match_history.append(match_history_object)
            elif team_num == 3:
                match_object.opponent.match_history.append(match_history_object)
            else:
                return

        team_num += 1


def process_head_to_head(head_to_head, match_object):
    boxes = head_to_head.find_all("div", class_="flexbox-column")

    team_wins = 0
    overtimes = 0
    opponent_wins = 0

    box_num = 0
    for box in boxes:
        number = int(box.find("div", class_="bold").string)
        if box_num == 0:
            team_wins = number
        elif box_num == 1:
            overtimes = number
        elif box_num == 2:
            opponent_wins = number
        else:
            break

    match_object.team_wins = team_wins
    match_object.overtimes = overtimes
    match_object.opponent_wins = opponent_wins


def process_analytics(analytics, match_object):
    analytics_link = analytics.find("a", class_="matchpage-analytics-center-container")["href"]

    page = requests.get(base_url + analytics_link)
    analytics_page = BeautifulSoup(page.content, "html.parser")
    player_stats = analytics_page.find_all("div", class_="analytics-player-container")
    map_details = analytics_page.find_all("div", class_="analytics-handicap-map-data-bottom")

    process_player_ratings(player_stats, match_object)
    process_map_details(map_details, match_object)


def process_player_ratings(player_stats, match_object):
    team_num = 0
    team_player_ratings = []
    opponent_player_ratings = []
    for team in player_stats:
        player_rating = team.find_all("td", class_="table-3-months")
        for player in player_rating:
            if team_num == 0:
                team_player_ratings.append(float(player.string))
            elif team_num == 1:
                opponent_player_ratings.append(float(player.string))
            else:
                raise Exception("More than 2 teams playing in analytics center")
        team_num += 1

    if len(team_player_ratings) < 5:
        for i in range(5 - len(team_player_ratings)):
            team_player_ratings.append(0.0)

    if len(opponent_player_ratings) < 5:
        for i in range(5 - len(opponent_player_ratings)):
            opponent_player_ratings.append(0.0)

    match_object.team.player_ratings = team_player_ratings
    match_object.opponent.player_ratings = opponent_player_ratings


def process_map_details(map_details, match_object):
    team_num = 0
    for table in map_details:
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        for row in rows:
            map_name = row.find("div", class_="mapname").string
            average_rounds = row.find_all("td", class_="analytics-handicap-map-data-avg")
            avg_rliw = average_rounds[0].string
            avg_rwil = average_rounds[1].string

            if avg_rliw == '-':
                avg_rliw = 14
            if avg_rwil == '-':
                avg_rwil = 0

            if team_num == 0:
                current_team = match_object.team
            elif team_num == 1:
                current_team = match_object.opponent
            else:
                raise Exception("More than 2 teams playing in analytics center")

            for current_map in current_team.get_maps():
                if current_map.get_name() != map_name:
                    continue
                current_map.set_rounds_lost_in_wins(float(avg_rliw))
                current_map.set_rounds_won_in_losses(float(avg_rwil))
        team_num += 1
        

