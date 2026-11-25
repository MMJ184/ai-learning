"""Night 6: print how many GitHub stars a few AI projects have.

First run `uv add tqdm` in the terminal. Then finish the two TODOs and run:
    uv run python scripts/github_stars.py
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
    # TODO 1: return the star count. Print data.keys() once to find the right key.
    raise NotImplementedError("TODO 1")


def main() -> None:
    # TODO 2: loop over REPOS wrapped in tqdm(...) to get a progress bar, call fetch_stars for each,
    # then print each repository with its stars, most stars first, like "pytorch/pytorch: 98,765"
    raise NotImplementedError("TODO 2")


if __name__ == "__main__":
    main()
