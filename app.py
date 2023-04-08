# import dependencies
import flask

# create a flask app
app = flask.Flask(__name__)

# create a route
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return flask.render_template('index.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True)