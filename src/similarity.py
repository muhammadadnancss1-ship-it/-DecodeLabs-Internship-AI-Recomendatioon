from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(user_profile: str, item_profiles: list[str]):
    """Return cosine similarity scores between the user profile and all items."""
    documents = [user_profile] + item_profiles

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    user_vector = vectors[0:1]
    item_vectors = vectors[1:]

    return cosine_similarity(user_vector, item_vectors).flatten()
