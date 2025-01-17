from intelxapi import intelx
from flask import Flask, request, jsonify
from q2config import *

# load api key
# the key should be defined in the q2config.py file
def search_darkweb(query, maxresults):
    intelx_object = intelx(intelx_key)
    result = intelx_object.search(query, maxresults = maxresults, buckets = ["darknet"])["records"]
    return result

# set up flask app
app = Flask(__name__)

# search endpoint
@app.route('/search', methods = ['POST'])
def search():
    data = request.get_json()
    query = data['query']
    maxresults = data.get('maxresults', 10)
    result = search_darkweb(query, maxresults)
    return jsonify(result)

if __name__ == '__main__':
    # the port and ip should be defined in the q2config.py file
    app.run(port = server_port, host = server_ip)
