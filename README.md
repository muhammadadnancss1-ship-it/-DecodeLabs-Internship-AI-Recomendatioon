1 AI Recommendation Engine

A simple content-based recommendation system built for DecodeLabs Artificial Intelligence Project 3.

The project takes user interests, compares them with a small course dataset, calculates similarity scores, and returns the most relevant course recommendations. It follows the basic recommendation pipeline: input, processing, scoring, sorting, and final Top-N output.

2 Project Goal

Create a recommendation system that:

- Takes user interests as input
- Matches those interests with available items
- Uses similarity logic to rank results
- Displays the best recommendations clearly

3 How It Works

The system uses content-based filtering. Each course has text information such as title, category, tags, description, and difficulty level. The user also enters interests like Python, machine learning, data analysis, automation, or web development.

Both the user interests and course information are converted into TF-IDF vectors. After that, cosine similarity is used to measure how close each course is to the user profile. The courses with the highest scores are shown first.


4 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity


Install requirements:

```bash
pip install -r requirements.txt
```

5 Run the Project

```bash
python main.py
```

6 Example Input

```text
Interest 1: Python
Interest 2: Machine Learning
Interest 3: AI
```

 Example Output

```text
Top recommendations for you:

1. Machine Learning Fundamentals - 45.36% match
2. Python for Data Analysis - 41.18% match
3. Advanced Machine Learning - 34.79% match
```

The final result is also saved inside:

```text
outputs/recommendations.txt
```

7 Dataset

The dataset is stored in:

```text
data/courses.csv
```

You can add more rows to this file to improve the recommendation results. Keep the same columns:

```text
id,title,category,tags,description,difficulty
```

8 Main Concepts Covered

- Recommendation system basics
- Content-based filtering
- User preference matching
- TF-IDF feature extraction
- Cosine similarity
- Ranking and filtering
- Top-N recommendations

9 Future Improvements

- Add user ratings
- Add more courses
- Build a Streamlit web interface
- Add category filters
- Store user history
- Compare content-based filtering with collaborative filtering

