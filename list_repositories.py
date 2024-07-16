import requests
import os

# Get credentials and target username or team from environment variables
username = os.getenv('BITBUCKET_USERNAME')
app_password = os.getenv('BITBUCKET_APP_PASSWORD')
target_username_or_team = os.getenv('BITBUCKET_TARGET_USERNAME_OR_TEAM')

if not username or not app_password or not target_username_or_team:
    print("Please set the environment variables: BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD, BITBUCKET_TARGET_USERNAME_OR_TEAM")
    exit(1)

url = f'https://api.bitbucket.org/2.0/repositories/{target_username_or_team}'

# Function to fetch repositories
def fetch_repositories(url, auth):
    repo_clone_urls = []
    while url:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            repositories = response.json()
            repo_clone_urls.extend(
                [repo['links']['clone'][0]['href'] for repo in repositories['values'] if 'https' in repo['links']['clone'][0]['href']]
            )
            url = repositories.get('next')
        else:
            print(f"Failed to retrieve repositories: {response.status_code}")
            break
    return repo_clone_urls

# Make the request
auth = (username, app_password)
repo_clone_urls = fetch_repositories(url, auth)

# Print the repository clone URLs
for repo_url in repo_clone_urls:
    print(repo_url)
