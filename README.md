Hello
# Bitbucket to GitHub Migration

This repository contains a Python script and a GitHub Actions workflow to automate the migration of repositories from a Bitbucket workspace to GitHub.

---

## Features

- Fetches repositories from a specified Bitbucket workspace using Bitbucket API.
- Clones repositories from Bitbucket with full history (`--mirror`).
- Create corresponding GitHub repositories using GitHub CLI and REST API.
- Pushes the cloned repositories to GitHub preserving history.
- Generates a CSV report summarizing migration status per repository.
- Uploads migration logs and reports as GitHub Action artifacts.

---

## Prerequisites

- Bitbucket Personal Access Token (PAT) with repository read access.
- GitHub Personal Access Token (PAT) with repo creation and push permissions.
- GitHub repository to host this migration workflow and script.

---

---

## Prerequisites (for manual/local testing)

- Python 3.x
- `git` and `gh` CLI tools
- Dependencies: `requests` (`pip install requests`)

---

## Setup

### 1. Add GitHub Secrets

Add the following secrets to your GitHub repository (Settings > Secrets and Variables > Actions):

| Secret Name          | Description                                  |
|----------------------|----------------------------------------------|
| `LGITHUB_PAT`        | GitHub Personal Access Token (PAT)           |
| `BITBUCKET_PAT`      | Bitbucket Personal Access Token (PAT)        |
| `GITHUB_ORGANISATION`| Your GitHub organization or username         |
| `BITBUCKET_KEY`      | (Optional) Bitbucket workspace key if needed  
| `ENTERPRISE_GIT_URL` | (Optional) Enterprise GitHub URL if used     |
| `ENTERPRISE_BITBUCKET_URL` | (Optional) Enterprise Bitbucket URL    |

> **Note:** `LGITHUB_PAT` is used instead of `GITHUB_PAT` due to naming restrictions.

### 2. Update `migration.yml` if needed

Make sure the environment variables in the workflow YAML (`migration.yml`) correctly reference your secrets, e.g.:

```yaml
env:
  GITHUB_PAT: ${{ secrets.LGITHUB_PAT }}
  BITBUCKET_PAT: ${{ secrets.BITBUCKET_PAT }}
  GITHUB_ORGANISATION: ${{ secrets.GITHUB_ORGANISATION }}
  BITBUCKET_KEY: ${{ secrets.BITBUCKET_KEY }}
  ENTERPRISE_GIT_URL: ${{ secrets.ENTERPRISE_GIT_URL }}
  ENTERPRISE_BITBUCKET_URL: ${{ secrets.ENTERPRISE_BITBUCKET_URL }}

  The workflow generates and uploads the following logs:

| File Name              | Purpose                                   |
|------------------------|-------------------------------------------|
| `github_migration.log` | Full log of the migration steps            |
| `migration_report.csv` | CSV report of success/failure per repo     |

> These can be downloaded from the **Artifacts** section of the workflow run.

---

## Log Preview

**migration_report.csv**
**github_migration.log**
