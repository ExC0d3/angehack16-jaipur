import os
from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['supporti']
collection = db['users']

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


# When developing locally, this will use port 5000,
# in production Heroku will set the PORT environment variable.

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
