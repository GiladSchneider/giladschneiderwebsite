# import dependencies
from flask import Flask, render_template, url_for

# create a Flask app
app = Flask(__name__)

# create a home route
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # get the main_image.jpeg file from the static folder
    image_file = url_for('static', filename='images/main_image.jpeg')
    return render_template('index.html', image_file=image_file)

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