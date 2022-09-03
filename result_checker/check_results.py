import requests
from bs4 import BeautifulSoup
from model import mongo_client
import time


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()

no_results = matches_doc.find({"prediction_correct": None})


for match in no_results:
    match_url = match["url"]

    # avoid rate limiting
    time.sleep(1)
    page = requests.get(match_url)
    soup = BeautifulSoup(page.content, "html.parser")

    result_box = soup.find("div", class_="standard-box teamsBox")
    if result_box is None:
        print("Result not yet ready for match " + match["team"]["name"] + " vs " + match["opponent"]["name"])
        continue
    team_scores = result_box.find_all("div", class_="team")

    for team_score in team_scores:
        team_name = team_score.find("div", class_="teamName")
        score = team_score.find("div", class_="won")
        if score is None:
            score = team_score.find("div", class_="lost")

        if score is None:
            break

        if match["team"]["name"] == team_name.string:
            matches_doc.update_one({"_id": match["_id"]}, {"$set": {"team_score": int(score.string)}})
        elif match["opponent"]["name"] == team_name.string:
            matches_doc.update_one({"_id": match["_id"]}, {"$set": {"opponent_score": int(score.string)}})
        else:
            raise Exception("Team not a part of this match " + team_name.string + " " + match_url)

    updated_match = matches_doc.find_one({"_id": match["_id"]})
    prediction_correct = False

    if "team_score" not in updated_match:
        print("Result not yet ready for match " + match["team"]["name"] + " vs " + match["opponent"]["name"])
        continue

    if updated_match["team_score"] > updated_match["opponent_score"]:
        if updated_match["prediction"] == updated_match["team"]["name"]:
            prediction_correct = True
    else:
        if updated_match["prediction"] != updated_match["team"]["name"]:
            prediction_correct = True

    print("Adding prediction result " + str(prediction_correct) + " for match " + updated_match["team"]["name"] + " vs " + updated_match["opponent"]["name"])
    matches_doc.update_one({"_id": updated_match["_id"]},
                           {"$set": {"prediction_correct": prediction_correct, "result_assessed": False}})

