# Bitbucket Repositories Fetcher

This script fetches the clone URLs of all repositories for a specified Bitbucket username or team, handling pagination if there are multiple pages of repositories.

## Prerequisites

- Python 3.x
- `requests` library

### Create a Python virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

You can install the `requests` library using pip:

```bash
pip install requests
```

### Setting Environment Variables
-> On Windows
Open Command Prompt and run:
```bash
set BITBUCKET_USERNAME=your_username
set BITBUCKET_APP_PASSWORD=your_app_password
set BITBUCKET_TARGET_USERNAME_OR_TEAM=target_username_or_team
```

-> On macOS/Linux
Open Terminal and run:
```bash
export BITBUCKET_USERNAME=your_username
export BITBUCKET_APP_PASSWORD=your_app_password
export BITBUCKET_TARGET_USERNAME_OR_TEAM=target_username_or_team
```

-> Run the script:

List all repositories.
```bash
python list_repositories.py
```

Fetch and clone all repositories in clone_repo folder.
```bash
python fetch_and_clone_repositories.py
```

# Troubleshooting
* Ensure you have set the environment variables correctly.
* Verify that your Bitbucket app password has the necessary permissions to read repositories.
* Check your internet connection and Bitbucket API status if you encounter network-related errors.
* If you receive a `401 Unauthorized` response, double-check your username and app password.
