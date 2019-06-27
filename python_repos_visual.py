import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make a call API and store the response.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
# Process results.
response_dict = r.json()
#print(f"Total repositories: {response_dict['total_count']}")
# Explore the information about the repositories.
repo_dicts = response_dict['items']
repo_names, stars = [], []
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub', 
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
#    print(key)

# Process results.
#print(response_dict.keys())

