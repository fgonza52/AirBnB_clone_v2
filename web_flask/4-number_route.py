#!/usr/bin/python3
'''
Starts a Flask web application listening on 0.0.0.0, port 5000

Extra requirement:
/python/(<text>): display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space)
The default value of text is “is cool”

$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:
$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Defines body of response to GET request to `root` location'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Defines body of response to GET request to `hbnb` location'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Defines body of response to GET request to `c/<text>` location'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    '''
    Defines body of response to GET request to `python/` and `python/<text>`
    '''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''TODO'''
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
