# Import Flask class from flask library. (Note the upper/lowercase convention.)
from flask import Flask, render_template

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# sitting up the route ddecorator
# The default URL ends in / ("my-website.com/").
# Could be instead "my-website.com/about" or anything - more on this later.
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
    skills = ['Javascript','Express','Python']
    return render_template("index.html", greeting="Hello World!", skills=skills)

@app.route('/sayhi/<username>') # When someone goes here...
def hello(username): # Do this.
    return "Hello {}".format(username)
# Run the app when we call this file
if __name__ == '__main__':
    app.run(debug=True)