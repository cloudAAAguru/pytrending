import requests
import csv

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
lines = []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_stars = repo_dict['stargazers_count']
    line = f'{repo_name},{repo_url},{repo_stars}'
    lines.append(line.split(','))
    print(line) 

# Dump into CSV file
filename='python_popular_repos.csv'
headers= 'Repo Name,Repo URL,Repo Stars'
with open(filename,'w',newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers.split(','))
    writer.writerows(lines)