# Main application of coding test endpoint

from flask import Flask
from route.problem1 import problem1
from route.problem2 import problem2
from route.problem3 import problem3

app = Flask(__name__)

app.register_blueprint(problem1, url_prefix='/problem1/')
app.register_blueprint(problem2, url_prefix='/problem2/')
app.register_blueprint(problem3, url_prefix='/problem3/')

@app.route('/')
def hello_flask():
    return 'This is Flask App for Coding Test Case'

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)