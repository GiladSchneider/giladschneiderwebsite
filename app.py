# import dependencies
from flask import Flask, render_template, url_for
import torch

# create a Flask app
app = Flask(__name__)

# create a home route
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    # get the main_image.jpeg file from the static folder
    return str(torch.__version__)
    # return render_template('index.html')

# create a research route
@app.route('/research', methods=['GET'])
def research():
    return render_template('research.html')

# create a projects route
@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')

# create a games route
@app.route('/games', methods=['GET'])
def games():
    return render_template('games.html')

# create a cv route
@app.route('/cv', methods=['GET'])
def cv():
    return render_template('cv.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True) 