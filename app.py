# import dependencies
from flask import Flask, render_template

# create a Flask app
app = Flask(__name__)

# create a home route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True) 