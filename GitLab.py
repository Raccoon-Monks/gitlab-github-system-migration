from time import sleep
from wget import download

import json
import requests


class GitLab:
    def __init__(self, token) -> None:
        gitlab_url_base = 'https://gitlab.com/api'
        gitlab_groups_endpoint = '/v4/groups/'
        gitlab_projects_endpoint = '/v4/projects/'
        self.gitlab_groups = f'{gitlab_url_base}{gitlab_groups_endpoint}'
        self.gitlab_projects = f'{gitlab_url_base}{gitlab_projects_endpoint}'

        self.raccoon = 'devraccoon'
        self.token = token
        self.slash = '%2F'
        self.projects_raw = {}
        self.projects = []


    def get_subgroup_repositories(self, subgroup: str = 'netsuite', per_page: int = 100) -> None:
        url = (
            f'{self.gitlab_groups}{self.raccoon}{self.slash}{subgroup}'
            f'/projects?per_page={per_page}')

        res = requests.get(
            url=url,
            headers={ 'Authorization': f'Bearer {self.token}' },
            params={ 'include_subgroups' : True })

        self.projects_raw = json.loads(res.text)


    def compose_repositories_info(self) -> dict:
        for project in self.projects_raw:
            file_name = project['path_with_namespace'].replace('/', '_')

            self.projects.append({
                'id': project['id'],
                'name_with_namespace': project['name_with_namespace'],
                'path_with_namespace': project['path_with_namespace'],
                'http_url_to_repo': project['http_url_to_repo'],
                'output_file': f'./gitlab_repositories/{file_name}.zip'
            })

        return self.projects


    def download_repositories(self, extension: str = 'zip') -> None:       
        for project in self.projects:
            id = project['id']

            repo_endpoint = f'/repository/archive.{extension}?private_token='
            url = f'{self.gitlab_projects}{id}{repo_endpoint}{self.token}'
            output_file = project['output_file']

            download(url=url, out=output_file)
            print(f'\nSuccess! File Downloaded {output_file}')
            sleep(1)


    @staticmethod
    def log(
        obj_to_log: dict, 
        file_name: str = 'log',
        extension: str = 'json') -> None:
        f = open(file=f'{file_name}.{extension}', mode='w')
        f.write(json.dumps(obj=obj_to_log, indent=4))
        f.close()


    @staticmethod
    def farewell() -> None:
        msg = (
            'I had my reasons for moving on\n'
            'These days liquor don\'t write my son\n'
            '\n'
            'It ain\'t right for a family man\n'
            'To build a house on shifting sand\n'
            'But don\'t think that I\'ve given up\n'
            'I\'m just takin\' on the harder stuff.')

        print(msg)
