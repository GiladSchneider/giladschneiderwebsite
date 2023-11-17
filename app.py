# import dependencies
from flask import Flask, render_template, url_for

# create a Flask app
app = Flask(__name__)

# create a home route
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# create a projects route
@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')

# create a cv route
@app.route('/cv', methods=['GET'])
def cv():
    return render_template('cv.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True) 