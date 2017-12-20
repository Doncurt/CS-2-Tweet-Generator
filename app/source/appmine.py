from flask import Flask
from stochsample import weight_sampling
from histogram import histo
from markovChain import nth_order_markov_dictograms,nth_order_markov
app = Flask(__name__)

@app.route('/')
def index():
    test = 'green fish one fish two fish red fish blue '



    fish_test = nth_order_markov_dictograms(test, 4)

    return nth_order_markov(fish_test)

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)
