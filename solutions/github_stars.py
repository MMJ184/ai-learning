"""Night 6 solution: print how many GitHub stars a few AI projects have.

    uv run python solutions/github_stars.py
"""

import json
from urllib.request import Request, urlopen

from tqdm import tqdm

REPOS = ["pytorch/pytorch", "huggingface/transformers", "scikit-learn/scikit-learn"]


def fetch_stars(repo: str) -> int:
    """Return the number of stars of a GitHub repository named like "owner/name"."""
    request = Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "ai-learning"},
    )
    with urlopen(request, timeout=10) as response:
        data = json.load(response)
    return data["stargazers_count"]


def main() -> None:
    stars = {}
    for repo in tqdm(REPOS, desc="Fetching"):
        stars[repo] = fetch_stars(repo)
    for repo, count in sorted(stars.items(), key=lambda item: -item[1]):
        print(f"{repo}: {count:,}")


if __name__ == "__main__":
    main()
