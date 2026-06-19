import re

import pandas as pd


SPACE_PATTERN = re.compile(r"\s+")


def clean_text(value: str) -> str:
    """Keep the text simple and consistent before vectorizing it."""
    text = str(value).lower().strip()
    text = re.sub(r"[^a-z0-9+#. ]", " ", text)
    text = SPACE_PATTERN.sub(" ", text)
    return text


def build_course_profile(courses: pd.DataFrame) -> pd.Series:
    """Combine the fields that describe each course into one searchable profile."""
    combined_text = (
        courses["title"].astype(str)
        + " "
        + courses["category"].astype(str)
        + " "
        + courses["tags"].astype(str)
        + " "
        + courses["description"].astype(str)
        + " "
        + courses["difficulty"].astype(str)
    )

    return combined_text.apply(clean_text)


def build_user_profile(interests: list[str]) -> str:
    """Turn user interests into the same text style used for course profiles."""
    return clean_text(" ".join(interests))
