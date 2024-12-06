import requests
# from parse_html import html_parse
# import html_parse
# from save_data import save_data

# Website to scrape
url = input("input your url")
response = requests.get(url)
if response.status_code == 200:
    print("Page fetch successfully")
    print(response.text[:500])

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find_all('a', class_='storylink')  # Example for Hacker News
for headline in headlines:
    print(headline.text, headline['href'])


import json

data = [{"title": headline.text, "url": headline['href']} for headline in headlines]
with open("news.json", "w") as file:
    json.dump(data, file, indent=4)


import argparse

parser = argparse.ArgumentParser(description="News Aggregator")
parser.add_argument("--category", type=str, help="Specify news category (e.g., tech, science)")
args = parser.parse_args()

# Handle category-specific logic here
print(f"Fetching {args.category} news...")


