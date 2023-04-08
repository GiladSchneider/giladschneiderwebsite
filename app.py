# import dependencies
import flask

# create a flask app
app = flask.Flask(__name__)

# create a route
@app.route('/')
@app.route('/home')
def home():
    # return flask.render_template('index.html')
    return 'Hello World'

# run the app
if __name__ == '__main__':
    app.run()