import os
import subprocess
import requests

BITBUCKET_WORKSPACE = "professionalworkspace"
GITHUB_USERNAME = "lakshmiganapathii"

def get_bitbucket_repos():
    repos = []
    url = f"https://api.bitbucket.org/2.0/repositories/{BITBUCKET_WORKSPACE}?pagelen=100"
    while url:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        for repo in data["values"]:
            repos.append(repo["slug"])
        url = data.get("next")
    return repos

def create_github_repo(repo_name):
    print(f"Creating GitHub repo: {repo_name}")
    cmd = [
        "gh", "repo", "create", f"{GITHUB_USERNAME}/{repo_name}",
        "--public", "--confirm"
    ]
    subprocess.run(cmd, check=True)

def migrate_repo(repo_name):
    clone_url = f"https://bitbucket.org/{BITBUCKET_WORKSPACE}/{repo_name}.git"
    print(f"Cloning {clone_url}")
    subprocess.run(["git", "clone", "--mirror", clone_url], check=True)

    os.chdir(f"{repo_name}.git")
    target_url = f"https://github.com/{GITHUB_USERNAME}/{repo_name}.git"
    print(f"Pushing to GitHub: {target_url}")
    subprocess.run(["git", "push", "--mirror", target_url], check=True)
    os.chdir("..")
    subprocess.run(["rm", "-rf", f"{repo_name}.git"])

def main():
    repos = get_bitbucket_repos()
    for repo in repos:
        try:
            print(f"\n📦 Migrating repo: {repo}")
            create_github_repo(repo)
        except subprocess.CalledProcessError:
            print(f"Repo {repo} may already exist. Skipping creation.")
        try:
            migrate_repo(repo)
        except Exception as e:
            print(f"❌ Migration failed for {repo}: {e}")

if __name__ == "__main__":
    main()