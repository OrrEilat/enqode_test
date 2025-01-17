# Setting up the API

- Install python 3.
- Install the python libraries flask and intelx.
- Open the q2config.py to set up the intelx credentials, as well server ip and port.
- Run server.py.

# Using the API
Send a request to the server's url + '/search'.
The message body should contain a Json object with the fields:
- query: The domain or company name to query.
- maxresults (optional): a limit to the number of search results to receive.

<code>

curl -X POST http://localhost:5555/search -H "Content-Type: application/json" -d "{\"query\":\"example.com\"}"

</code>

The returned object will be a list of record objects: [record_1, record_2, etc...]
