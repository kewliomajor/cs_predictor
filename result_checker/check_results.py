import requests
from bs4 import BeautifulSoup
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
cs_matches_db = client["cs_matches"]
matches_doc = cs_matches_db["matches"]

no_results = matches_doc.find({"prediction_correct": None})


for match in no_results:
    match_url = match["url"]
    page = requests.get(match_url)
    soup = BeautifulSoup(page.content, "html.parser")

    result_box = soup.find("div", class_="standard-box teamsBox")
    team_scores = result_box.find_all("div", class_="team")

    for team_score in team_scores:
        team_name = team_score.find("div", class_="teamName")
        score = team_score.find("div", class_="won")
        if score is None:
            score = team_score.find("div", class_="lost")

        if match["team"]["name"] == team_name.string:
            matches_doc.update_one({"_id": match["_id"]}, {"$set": {"team_score": int(score.string)}})
        elif match["opponent"]["name"] == team_name.string:
            matches_doc.update_one({"_id": match["_id"]}, {"$set": {"opponent_score": int(score.string)}})
        else:
            raise Exception("Team not a part of this match " + team_name.string + " " + match_url)

    updated_match = matches_doc.find_one({"_id": match["_id"]})

    if updated_match["team_score"] > updated_match["opponent_score"]:
        if updated_match["prediction"] == updated_match["team"]["name"]:
            matches_doc.update_one({"_id": updated_match["_id"]}, {"$set": {"prediction_correct": True, "result_assessed": False}})
        else:
            matches_doc.update_one({"_id": updated_match["_id"]}, {"$set": {"prediction_correct": False, "result_assessed": False}})
    else:
        if updated_match["prediction"] == updated_match["team"]["name"]:
            matches_doc.update_one({"_id": updated_match["_id"]}, {"$set": {"prediction_correct": False, "result_assessed": False}})
        else:
            matches_doc.update_one({"_id": updated_match["_id"]}, {"$set": {"prediction_correct": True, "result_assessed": False}})

