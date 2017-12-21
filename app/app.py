import os

from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append('/Users/donovanadams/desktop/GitHub/CS-2-Tweet-Generator/app/source')
sys.path.append('/Users/donovanadams/desktop/GitHub/CS-2-Tweet-Generator/app/')
from markovChain import Markov
from stripText import Clean

file_name = "histogram.txt"
data = Clean().clean_text(file_name)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    tweet_markov = Markov().nth_order_markov_dictograms(data, 8)
    tweet_it = Markov().nth_order_markov(tweet_markov)
    return render_template('home.html', tweet = tweet_it )


@app.route('/about/')
def about():
    """Render the website's about page."""
    tweet_markov = Markov().nth_order_markov_dictograms(data, 8)
    tweet_it = Markov().nth_order_markov(tweet_markov)
    return render_template('about.html', tweet = tweet_it)



@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

    
