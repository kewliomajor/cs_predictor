import requests
import match_processor
from bs4 import BeautifulSoup
from model import mongo_client
import json
from json import JSONEncoder
import time


class CsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


print_only = True
client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()

base_url = "https://www.hltv.org"

url = base_url + "/matches"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

todays_matches = soup.find("div", class_="upcomingMatchesSection")

matches = todays_matches.find_all("div", class_="upcomingMatch")

match_urls = []

for match in matches:
    match_link = match.find("a", class_="match")
    match_url = match_link["href"]
    match_urls.append(base_url + match_url)

for url in match_urls:
    existing = matches_doc.find_one({"url": url})
    if existing is not None:
        continue

    # avoid rate limiting
    time.sleep(1)
    page = requests.get(url)
    match_page = BeautifulSoup(page.content, "html.parser")
    match_object = match_processor.process_match(match_page)
    match_object.url = url

    if match_object.team.name is None or match_object.opponent.name is None:
        print("Match is missing 1 or more participants: " + url)
        continue
    print("Adding match " + match_object.team.name + " vs " + match_object.opponent.name)
    if print_only:
        print(to_dict(match_object))
    else:
        matches_doc.insert_one(to_dict(match_object))
