import os
import requests
from dotenv import load_dotenv
load_dotenv()

SESSION_COOKIE = os.getenv("SESSION_COOKIE")

def get_data(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    auth = {"session": SESSION_COOKIE}
    USER_AGENT = {"User-Agent": "advent-of-code-data v0.8.5"}
    response = requests.get(url, cookies=auth, headers=USER_AGENT)
    data = response.text.strip()
    return data

def print_answers(dict):
    print("1st Challenge: ", dict['first'])
    if dict['second']:
        print("2nd Challenge: ", dict['second'])

answers = {"first": 0, "second": 0}
