#!webapi/bin/python

from flask import Flask, jsonify, request
import pyodbc


class memestat:
	
	pass 
	







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
#
@app.route('/api/memes', methods=['GET'])
def getMeme(start, end):
    # Once Jacob gets the database setup, this function will get data from it.
    # Right now, though, we'll just use fake data.
    pass




@app.route('/api/MemeStats',  methods=['GET'])
def getAllMemes():
	start = request.args.get('start')
	end = request.args.get('end')
	return jsonify({'start' : start, 'end':end})	





if __name__ == '__main__':
    app.run(debug=True)
