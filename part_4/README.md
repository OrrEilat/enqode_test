# Setting up the server
- Ensure you have Python and Flask installed.
- Open the 'q4config.py' to set up the server's ip and port.
- Run 'server.py' to start the server.
- The data will be saved in 'data.db'

# API Endpoints documentation
Endpoint: <code>/store</code>

Method: <code>POST</code>

Description: Accepts Zero-Trust Score data in JSON format and stores it.

Body: A json object to store

<hr>

Endpoint: <code>/retrieve</code>

Method: <code>GET</code>

Description: Responds with a json object containing all the stored data.

# Example cURL calls

Store:
```
curl -X POST http://localhost:5000/store -H "Content-Type: application/json" -d "json-data-to-store"
```

Retrieve:
```
curl -X GET http://localhost:5000/retrieve
```


