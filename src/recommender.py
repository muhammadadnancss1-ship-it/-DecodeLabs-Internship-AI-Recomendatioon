import pandas as pd

from .preprocess import build_course_profile, build_user_profile
from .similarity import calculate_similarity


def recommend_courses(courses: pd.DataFrame, interests: list[str], top_n: int = 5) -> pd.DataFrame:
    """Score all courses and return the most relevant recommendations."""
    if len(interests) < 3:
        raise ValueError("Please provide at least three interests for better recommendations.")

    course_profiles = build_course_profile(courses)
    user_profile = build_user_profile(interests)
    scores = calculate_similarity(user_profile, course_profiles.tolist())

    ranked_courses = courses.copy()
    ranked_courses["similarity_score"] = scores
    ranked_courses = ranked_courses.sort_values("similarity_score", ascending=False)

    return ranked_courses.head(top_n).reset_index(drop=True)
