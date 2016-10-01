#!webapi/bin/python

from flask import Flask, jsonify
import pyodbc


app = Flask(__name__, static_url_path='/static')

# This route is for loading the web app. All the javasctipt/html is then loaded
# from index.html.
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def send_js(path):
    return app.send_static_file(path)


# This is the endpoint that returns all of the memes from the database.
@app.route('/api/memes', methods=['GET'])
def get_meme():
    # Once Jacob gets the database setup, this function will get data from it.
    # Right now, though, we'll just use fake data.
    memes = [
        {
            'id': 1,
            'name': u'Harambe',
            'image': u'Harambe image', 
        },
        {
            'id': 2,
            'name': u'Pepe',
            'image': u'Pepe image', 
        },
    ]
    return jsonify({'memes': memes})

if __name__ == '__main__':
    app.run(debug=True)
