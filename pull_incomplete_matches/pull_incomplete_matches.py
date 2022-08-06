import requests
import match_processor
from bs4 import BeautifulSoup
from model import mongo_client
import json
from json import JSONEncoder


class CsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


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
    page = requests.get(url)
    match_page = BeautifulSoup(page.content, "html.parser")
    match_object = match_processor.process_match(match_page)
    match_object.url = url

    matches_doc.insert_one(to_dict(match_object))
