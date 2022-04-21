import sys
import pandas as pd
import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf



def recommend_movies(selected_user_id, model):
    pred = pd.read_csv("all_movies.csv")
    pred["user_id"] = selected_user_id
    
    pred["rating"] = model.predict([pred["user_id"], pred["movie_id"]])
    user_watched_movies = pd.read_csv("user_watched_movies.csv")
    
    watched_movies = eval(user_watched_movies[user_watched_movies.user_id == selected_user_id].movie_id.values[0])
    pred["watched"] = pred["movie_id"].apply(lambda x: int(x in watched_movies))
    return pred[pred.watched == 0].sort_values("rating", ascending=False)[:5].movie_title.values


if __name__ == "__main__":
    MIN_USER_ID, MAX_USER_ID = 1, 6040

    if len(sys.argv) != 2:
        print("Syntax for this scripts is: python predict.py USER_ID")
        print("Please run again...")
        exit()
    
    selected_user_id = sys.argv[1]
    try:
        selected_user_id = int(selected_user_id)
    except:
        print("User ID must be an integer")
        exit()

    if (selected_user_id < MIN_USER_ID) or (selected_user_id > MAX_USER_ID):
        print(f"User ID range: [{MIN_USER_ID, MAX_USER_ID}]")
        exit()

    model = tf.keras.models.load_model("best_model.h5")

    preds = recommend_movies(selected_user_id, model)
    
    print(f"Recommendation for user {selected_user_id}:")
    for i, pred in enumerate(preds):
        print(f"{i+1}.\t {pred}")