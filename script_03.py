import json, wget

f = open(file='backoffice_ti_projects.json', mode='r')
subgroups = json.loads(f.read())
f.close()

for subgroup in subgroups:
    length = len(subgroups[subgroup])
    
    if length > 0:
        projects = subgroups[subgroup]
        
        for project in projects:
            id = project['id']
            url = project['http_url_to_repo']
            print(f'ID: {id} | URL: {url}')

            base = 'https://gitlab.com/api/v4/projects/'
            endpoint = '/repository/archive.zip?private_token='
            token = 'YOUR_TOKEN_HERE'
            url = f'{base}{id}{endpoint}{token}'

            wget.download(url)