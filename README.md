# AI learning: month 1

My nightly AI practice, 9:00–11:00 PM IST, from 23 November to 20 December 2026: Python, NumPy and pandas,
the math behind machine learning, and scikit-learn.

Study guide with every night's lesson: [AI Learning Plan](https://claude.ai/artifact/5MJxvaW9sNxjp7rjmPWuCu)

## What's here

| Path | What it is |
| --- | --- |
| `notebooks/` | One practice notebook per week. Run each exercise cell; its checks print ✅ Correct when it works. |
| `solutions/` | Worked answers. Open only after 20 minutes of being stuck. |
| `data/` | `penguins.csv`, `tips.csv` and `titanic.csv`, used all month. |
| `scripts/` | Small Python scripts, starting with `github_stars.py` on Night 6. |
| `check_setup.py` | Night 1 check that Python, the libraries and the data are ready. |
| `notes.md` | Three lines of notes each night. |

## Every night

1. `git pull` (in case you worked on the other laptop)
2. Learn for 50 minutes from the study guide, break for 10, then practice for 50 minutes in the week's notebook
3. Write three lines in `notes.md`
4. `git add .`, `git commit -m "Night N: topic"`, `git push`

## Commands

| Task | Command |
| --- | --- |
| Install Python and every library | `uv sync` |
| Check the setup | `uv run python check_setup.py` |
| Add a library | `uv add <name>` |
| Run a script | `uv run python scripts/github_stars.py` |

In VS Code, pick the `.venv` kernel (Python 3.13) at the top right of a notebook.

## Month 1 results

Paste your Night 28 results table here.

## Data sources

- Penguins: Palmer Penguins by Allison Horst, Alison Hill and Kristen Gorman (CC0), via the seaborn-data repository
- Tips and Titanic: the seaborn-data example datasets
