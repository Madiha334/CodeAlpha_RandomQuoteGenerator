
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Quotes ki list
quotes = [
    {
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt"
    },
    {
        "quote": "Success is not final; failure is not fatal: It is the courage to continue that counts.",
        "author": "Winston Churchill"
    },
    {
        "quote": "The way to get started is to quit talking and begin doing.",
        "author": "Walt Disney"
    },
    {
        "quote": "Innovation distinguishes between a leader and a follower.",
        "author": "Steve Jobs"
    },
    {
        "quote": "Your time is limited, so don't waste it living someone else's life.",
        "author": "Steve Jobs"
    },
    {
        "quote": "Code is like humor. When you have to explain it, it’s bad.",
        "author": "Cory House"
    }
]

@app.route('/')
def home():
    # Pehli dafa page khulne par aik random quote uthana
    initial_quote = random.choice(quotes)
    return render_template('index.html', quote=initial_quote)

@app.route('/get-quote', methods=['GET'])
def get_quote():
    # Button click par AJAX/Fetch ke zariye naya quote JSON format mein bhejna
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)