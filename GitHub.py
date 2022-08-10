from urllib import request
import requests


class GitHub:
    def __init__(self, token) -> None:
        self.accees_token = token
        self.url_github = 'https://api.github.com'

        self.endpoint_create_repositories = '/orgs/raccoon-monks/repos'
        self.endpoint_list_organizarion_repositories = '/orgs/Raccoon-Monks/repos'

        self.url_create_repositories = f'{self.url_github}{self.endpoint_create_repositories}'
        self.url_list_organizarion_repositories = f'{self.url_github}{self.endpoint_list_organizarion_repositories}'


    def createRepository(self, repository_name) -> None:
        header = {
            'Accept': 'application/vnd.github+json',
            'Authorization': self.accees_token,            
            'body': {
                'name': repository_name, 
                'description': 'This is your first repository'
            }
        }        

        requests.post(url=self.url_create_repositories, headers=header)


    def listOrganizationRepositories(self) -> dict:
        header = {
            'Accept': 'application/vnd.github+json',
            'Authorization': self.accees_token
        }

        response = requests.get(url=self.url_list_organizarion_repositories, headers=header)

        return response

