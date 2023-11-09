from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__) 

boostrap = Bootstrap5(app)

# home
@app.route('/')
def hello(): 
    return render_template('index.html')