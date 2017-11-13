from flask import Flask
from stochsample import weight_sampling
from histogram import histo
app = Flask(__name__)

@app.route('/')
def index():
    return weight_sampling(histo)

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)
