"""Night 1 check: confirms Python, the libraries and the datasets are ready.

Run it from the project folder:  uv run python check_setup.py
"""

import sys
from importlib import import_module
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIBRARIES = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "ipykernel"]
DATASETS = ["penguins.csv", "tips.csv", "titanic.csv"]


def main() -> int:
    problems = []
    print(f"Python {sys.version.split()[0]} ({sys.executable})")
    if sys.version_info < (3, 12):
        problems.append("Python 3.12 or newer is needed: run `uv sync` inside the project folder.")
    if ".venv" not in sys.prefix:
        print("Tip: run this with `uv run python check_setup.py` so it uses the project's environment.")

    for name in LIBRARIES:
        try:
            module = import_module(name)
            print(f"  ok  {name} {getattr(module, '__version__', '')}")
        except ImportError:
            problems.append(f"{name} is missing: run `uv sync`, then try again with `uv run`.")

    for file in DATASETS:
        if (ROOT / "data" / file).exists():
            print(f"  ok  data/{file}")
        else:
            problems.append(f"data/{file} is missing: unzip the starter project again.")

    if problems:
        print("\nNot ready yet:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("\nSetup works")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
