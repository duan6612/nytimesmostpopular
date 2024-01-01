######################################################
#   Author: Muhammad Ridhwan Hakeem bin Khairrazi    #
#      Title: NY Times Most Popular Articles         #
######################################################

# Import necessary libraries
import requests
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# API key for accessing NY Times Most Popular Articles API
api_key = "GU6Aru9bt7OtVZrbpt3wy6hNiV2A8Su0"  
# API endpoint URL
api_url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json"

# Function to fetch most popular articles
def get_most_popular_articles(api_key):
    params = {"api-key": api_key}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])
        return articles
    else:
        return None

# Route for the homepage
@app.route('/')
def home():
    articles = get_most_popular_articles(api_key)
    enumerated_articles = list(enumerate(articles))
    return render_template('index.html', enumerated_articles=enumerated_articles)

# Route to show details when an item is clicked
@app.route('/article/<int:index>')
def show_article_details(index):
    articles = get_most_popular_articles(api_key)
    if articles and 0 <= index < len(articles):
        article = articles[index]
        return render_template('article_details.html', article=article)
    else:
        return "Article not found."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
