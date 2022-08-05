import json, requests

gitlab = 'https://gitlab.com/api/v4/groups/devraccoon/subgroups'

res = requests.get(
    url=gitlab,
    headers={ 'Authorization': 'Bearer YOUR_TOKEN_HERE' }
)

res_json = json.loads(s=res.text)

f = open('response.json', 'w')
f.write(json.dumps(res_json, indent=2))
f.close()