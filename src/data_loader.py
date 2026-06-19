from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"id", "title", "category", "tags", "description", "difficulty"}


def load_courses(file_path: str | Path) -> pd.DataFrame:
    """Load course data and check that the CSV has the columns we need."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    courses = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS.difference(courses.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Dataset is missing required columns: {missing}")

    return courses.fillna("")
