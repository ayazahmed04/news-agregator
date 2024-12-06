from bs4 import BeautifulSoup

def html_parse(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('a', class_='storylink')
    for headline in headlines:
        print(headline.text, headline['href'])
    
# Sent data to other line
import json 
def save_data(headline):
    data = [{'title': headline.text, 'url':headline['href'], } for headlines in headline]
    with open('news.json', 'w') as file:
        json.dump(data, file, indent=4)

save_data(headlines)