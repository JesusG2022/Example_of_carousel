from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__) 

boostrap = Bootstrap5(app)

# home
@app.route('/')
def home(): 
    return render_template('FirstPage.html')

def Men(): 
    return render_template('SecondPage.html')

def Athlete(): 
    return render_template('ThirdPage.html')

def First_Responders(): 
    return render_template('FourthPage.html')

def Teen(): 
    return render_template('FifthPage.html')
