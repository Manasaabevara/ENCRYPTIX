import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Create a small dataset of movies and ratings
data = {
    'userId': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'movieId': [101, 102, 103, 101, 102, 104, 101, 103, 104, 102, 103, 104],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie A', 'Movie B', 'Movie D', 'Movie A', 'Movie C', 'Movie D', 'Movie B', 'Movie C', 'Movie D'],
    'rating': [5, 4, 3, 4, 5, 2, 2, 4, 5, 4, 3, 5]
}

# Convert the dictionary to a DataFrame
ratings = pd.DataFrame(data)

# Display the first few rows of the dataset
print(ratings)
# Create a user-item matrix
user_movie_matrix = ratings.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN values with 0
user_movie_matrix = user_movie_matrix.fillna(0)

# Compute the cosine similarity matrix
user_similarity = cosine_similarity(user_movie_matrix)

def recommend_movies(user_id, user_movie_matrix, user_similarity, n_recommendations=5):
    # Get the similarity scores for the given user
    user_idx = user_id - 1  # Adjusting for 0-based index
    sim_scores = user_similarity[user_idx]
    
    # Get the indices of the most similar users
    similar_users = np.argsort(sim_scores)[::-1]
    
    # Get the movies watched by the most similar users
    recommended_movies = []
    for similar_user in similar_users:
        if similar_user == user_idx:
            continue
        similar_user_movies = user_movie_matrix.iloc[similar_user]
        recommended_movies.extend(similar_user_movies[similar_user_movies > 0].index.tolist())
        if len(recommended_movies) >= n_recommendations:
            break
    
    # Return the top n recommendations
    return list(set(recommended_movies[:n_recommendations]))

# Make recommendations for a specific user
user_id = int(input("Enter user_id: "))
recommendations = recommend_movies(user_id, user_movie_matrix, user_similarity)
print(f"Recommendations for user {user_id}: {recommendations}")
