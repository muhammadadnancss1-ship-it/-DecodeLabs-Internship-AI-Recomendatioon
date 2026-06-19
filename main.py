from pathlib import Path

from src.data_loader import load_courses
from src.predict import collect_interests
from src.recommender import recommend_courses


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = r"E:\New folder (6)\ai_recommendation_engine\ai_recommendation_engine\data\courses.csv"
OUTPUT_PATH = BASE_DIR / "outputs" / "recommendations.txt"


def save_recommendations(recommendations, interests: list[str]) -> None:
    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    lines = []
    lines.append("AI Recommendation Engine Results")
    lines.append("=" * 34)
    lines.append("")
    lines.append("User interests:")

    for interest in interests:
        lines.append(f"- {interest}")

    lines.append("")
    lines.append("Recommended courses:")

    for index, row in recommendations.iterrows():
        rank = index + 1
        score = round(row["similarity_score"] * 100, 2)
        lines.append(f"{rank}. {row['title']} ({score}% match)")
        lines.append(f"   Category: {row['category']}")
        lines.append(f"   Difficulty: {row['difficulty']}")
        lines.append(f"   Why: {row['description']}")
        lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def print_recommendations(recommendations) -> None:
    print("\nTop recommendations for you:\n")

    for index, row in recommendations.iterrows():
        rank = index + 1
        score = round(row["similarity_score"] * 100, 2)
        print(f"{rank}. {row['title']} - {score}% match")
        print(f"   Category: {row['category']} | Difficulty: {row['difficulty']}")
        print(f"   {row['description']}\n")


def main() -> None:
    print("AI Recommendation Engine")
    print("Content-Based Filtering with TF-IDF and Cosine Similarity")
    print("-" * 64)

    courses = load_courses(DATA_PATH)
    interests = collect_interests(minimum=3)
    recommendations = recommend_courses(courses, interests, top_n=5)

    print_recommendations(recommendations)
    save_recommendations(recommendations, interests)

    print(f"Results saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
