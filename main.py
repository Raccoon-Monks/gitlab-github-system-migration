from GitLab import GitLab


gitlab = GitLab(token='YOUR_GITLAB_ACCESS_TOKEN_HERE')
gitlab.get_subgroup_repositories()
repo_info = gitlab.compose_repositories_info()
gitlab.log(obj_to_log=repo_info)
gitlab.download_repositories()