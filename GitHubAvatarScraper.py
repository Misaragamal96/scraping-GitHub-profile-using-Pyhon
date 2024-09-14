import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/misaragamal96"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)
# Note: This code will work correctly if the GitHub page contains the profile picture with the "Avatar" alt attribute.
# GitHubAvatarScraper: A simple script to scrape the profile picture from a GitHub profile using Python.
