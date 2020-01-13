import jwt

from flask import jsonify, request, make_response
from flask_restful import Resource

from ...api.controllers import format_response
from ..models import OAuthClient
from ... import db

class Authenticate(Resource):
    """ Validates user trough one the OAuth Providers, register, and generate access token """
    
    def post(self, handle):
        # Get provider authorization code
        auth_code = request.form.get("auth_code")
        if(not auth_code):
            return format_response("missing authorization code", 400)

        # Retrieve provider client data from db
        oauth_client = OAuthClient.query.filter(OAuthClient.client_handle == handle).first()
        if(not oauth_client):
            return format_response("client not found", 404)

        return make_response(
            jsonify({
                "data": oauth_client.client_handle
            }), 
            200
        )
        
        