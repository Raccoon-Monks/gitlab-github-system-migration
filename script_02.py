import json, re, requests

gitlab = 'https://gitlab.com/api/v4/groups/devraccoon%2fnetsuite/subgroups'

res = requests.get(
    url=gitlab,
    headers={ 'Authorization': 'Bearer YOUR_TOKEN_HERE' }
)

res_json = json.loads(s=res.text)
projects = []

for project in res_json:
    projects.append({
        'url' : project['web_url']
    }) 


for subgroup in projects:
    regex_pattern = r'https\:\/\/gitlab\.com\/groups\/devraccoon\/netsuite\/(.*)'
    regex = re.findall(pattern=regex_pattern, string=subgroup['url'])[0]
    url = f'https://gitlab.com/api/v4/groups/devraccoon%2fnetsuite%2f{regex}/projects'

    res = requests.get(
        url=url,
        headers={ 'Authorization': 'Bearer YOUR_TOKEN_HERE' }
    )

    res_json = json.loads(s=res.text)
    projects = []

    for project in res_json:
        projects.append({
            'id': project['id'],
            'name_with_namespace': project['name_with_namespace'],
            'path_with_namespace': project['path_with_namespace'],
            'http_url_to_repo': project['http_url_to_repo']
        })

        f = open(f'backoffice_ti_{regex}_projects.json', 'w')
        f.write(json.dumps(projects, indent=4))
        f.close()