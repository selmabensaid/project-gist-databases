import requests
from requests.exceptions import HTTPError

def import_gists_to_database(db, username, commit=True):
    params={
        'username':username
    }
    
    response=requests.get('https://api.github.com/users/{}/gists'.format(username))
    if not response.ok:
        raise HTTPError()
    gists=response.json()
    query= 'Insert into gists (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url) values (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, :comments_url) '
    if commit:
        for gist in gists:
            values={
                'github_id':gist['id'],
                'html_url': gist['html_url'],
                'git_pull_url': gist['git_pull_url'],
                'git_push_url': gist['git_push_url'],
                'commits_url': gist['commits_url'],
                'forks_url': gist['forks_url'],
                'public': gist['public'],
                'created_at': gist['created_at'],
                'updated_at': gist['updated_at'],
                'comments': gist['comments'],
                'comments_url': gist['comments_url']
            }
            db.execute(query, values)