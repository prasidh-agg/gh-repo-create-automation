#!/usr/bin/env python

import argparse
import requests
import json


def str_to_bool(s):
    return s.lower() == 'true'


def create_github_repo(repo_name, repo_description, is_private, is_auto_init):

    # pass your github token here
    github_token = ""
    
    # GitHub API endpoint for creating a repository
    api_url = "https://api.github.com/user/repos"

    # Set is_private based on user input
    is_private = not (is_private.lower() == "public")

    # Set is_auto_init based on user input
    is_auto_init = is_auto_init.lower() == "yes"

    # Build the payload
    payload = {
        "name": repo_name,
        "description": repo_description,
        "private": is_private,
        "auto_init": is_auto_init
    }

    # Headers with authorization
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {github_token}"
    }

    # Make the API request to create the repository
    response = requests.post(api_url, headers=headers,
                             data=json.dumps(payload))

    # Check the response status
    if response.status_code == 201:
        response_json = response.json()
        html_url = response_json.get("html_url")
        clone_url = response_json.get("clone_url")
        print("GitHub repository created successfully.")
        print(f"Link to visit the repository: {html_url}")
        print(f"Link to clone the repository: {clone_url}")
    else:
        print("Failed to create GitHub repository. Response:", response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a GitHub repository")
    parser.add_argument("repo_name", type=str, help="Repository name")
    parser.add_argument("repo_description", type=str,
                        help="Repository description")
    parser.add_argument("is_private", type=str,
                        help="Public or Private? (public/private)")
    parser.add_argument("is_auto_init", type=str,
                        help="Do you want to add a README file? (yes/no)")

    args = parser.parse_args()

    create_github_repo(args.repo_name, args.repo_description,
                       args.is_private, args.is_auto_init)
