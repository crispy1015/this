from textblob import TextBlob
def movie_review(summary):
    blob = TextBlob(summary)
    review = blob.sentiment.polarity 
    
    if review < 0:
        return "Negative"
    elif review == 0:
        return "Neutral"
    else:
        return "Positive"
    
movie_file = input("Enter the name of any film: ")

user_input = input(f"Write a review for {movie_file}: ") 
                   
polarity = movie_review(user_input)

file_extract = f"path/to/your/{movie_file}_review_with_sentiment.txt"

with open(file_extract, 'w') as extract_movie:
    extract_movie.write("Film: {movie_file}, Review: {user_input}, Sentiment: {polarity}\n ")

print(f"Film Title: {movie_file}, Review: {user_input}, Sentiment Score: {polarity}")
