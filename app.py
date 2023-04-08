# import dependencies
from flask import Flask, render_template

# create a Flask app for heroku
app = Flask(__name__)

# create a route for the app
@app.route('/', methods=['GET'])
def index():
    return "please go to /home"

# run the app
if __name__ == '__main__':
    app.run()