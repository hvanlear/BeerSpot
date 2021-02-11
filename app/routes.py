from flask import Flask, request, jsonify, render_template, make_response
from app import app
import us
from app.util import *
import requests


@app.errorhandler(500)
def serverError(error):
    return jsonify({'message': 'Brewery Query Not Found, Please try again'}), 500

@app.route('/')
@app.route('/index')
def index():
    states = us.states.STATES
    return render_template('index.html', states=states)

@app.route('/search', methods=['GET', 'POST'])
def search_brews():
    if request.method =='POST':
        req = request.form
        state = req.get('state')

    breweries = get_brew(state)
    return render_template('index.html', breweries=breweries)

@app.route('/breweries/<state>', methods = ['GET', 'POST'])
def show_state_brews(state):
    breweries =  get_state_info(state)
    res = make_response(breweries, 200)
    return res
 
    # return render_template('state.html', state =state, breweries = breweries)


