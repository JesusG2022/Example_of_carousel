# https://github.com/JesusG2022/Example_of_carousel/tree/main

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__) 

boostrap = Bootstrap5(app)

# home
@app.route('/')
def home(): 
    return render_template('homepage.html')
@app.route('/men')
def Men(): 
    return render_template('SecondPage.html')

@app.route('/Athlete')
def Athlete(): 
    return render_template('ThirdPage.html')

@app.route('/First_Responders')
def First_Responders(): 
    return render_template('FourthPage.html')

@app.route('/teen')
def teen(): 
    return render_template('FifthPage.html')
