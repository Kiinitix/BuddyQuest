import json
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import time
from threading import Thread


def load_adventure_data(filename='adventure_tracker.json'):
    with open(filename, 'r') as file:
        return json.load(file)


def prepare_data(data):
    adventure_list = []
    for date, activities in data.items():
        for adventure, count in activities.items():
            people, category = adventure.rsplit('-', 1)
            adventure_list.append({'people': people, 'category': category, 'count': count})
    return pd.DataFrame(adventure_list)


def train_recommendation_model(df):
    vectorizer = CountVectorizer()
    category_matrix = vectorizer.fit_transform(df['category'])
    similarity_matrix = cosine_similarity(category_matrix)
    df['similarity_score'] = similarity_matrix.mean(axis=1)
    return df, vectorizer


def save_model(df, vectorizer, model_filename='recommendation_model.pkl'):
    with open(model_filename, 'wb') as file:
        pickle.dump({'df': df, 'vectorizer': vectorizer}, file)


def load_model(model_filename='recommendation_model.pkl'):
    with open(model_filename, 'rb') as file:
        return pickle.load(file)


def recommend_adventure(df, user_friends):
    user_data = df[df['people'].str.contains(user_friends)]
    if user_data.empty:
        return ["No data available for this group. Try adding more adventures!"]
    
    top_adventures = user_data.sort_values(by='similarity_score', ascending=False).head(3)
    return top_adventures['category'].tolist()


def train_model_with_loading():
    print("Saved model not found. Training the recommendation model...")

    def loading_animation():
        while not model_ready:
            for char in "|/-\\":
                print(f"\rTraining model... {char}", end="", flush=True)
                time.sleep(0.2)
    
    global model_ready
    model_ready = False
    
    thread = Thread(target=loading_animation)
    thread.start()
    
    data = load_adventure_data()
    df = prepare_data(data)
    df, vectorizer = train_recommendation_model(df)
    save_model(df, vectorizer)
    
    model_ready = True
    thread.join()
    print("\rModel training complete!                              ")
    return df


def get_adventure_recommendations():
    try:
        model_data = load_model()
        df = model_data['df']

    except FileNotFoundError:
        df = train_model_with_loading()
    
    friends_group = input("Enter the friends group (e.g., Amit-Rahul): ")
    recommended_activities = recommend_adventure(df, friends_group)
    print(f"\nRecommended activities for {friends_group}: {recommended_activities}")


if __name__ == "__main__":
    get_adventure_recommendations()
