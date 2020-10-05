from app import *
from flask import Flask
import requests
import json
def test_base_route():
        app = Flask(__name__)
        connection_establish(app)
        client = app.test_client()
        url = '/'
        response = client.get(url)
        assert response.status_code == 200
def test_post_route__success():
        app = Flask(__name__)
        connection_establish(app)
        client = app.test_client()
        url =  "/threshold"
        mock_request_data = {"tvalue": "Create a Tweet"}       
        response = client.get(url,json=dict(tvalue="Create a Tweet"))
        assert response.status_code == 200


        #        assert b'Test Tweet posted from our tweet-Flask app ' in response.data
#        assert '<form' in response.data.decode('utf-8')
#        print(response.status_code,reponse.reason)
#        print(response.url)
